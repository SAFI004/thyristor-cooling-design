from mcp_client import FusionMCPClient
from pathlib import Path
import json
SCRIPT=r'''
import adsk, adsk.core as C, adsk.fusion as F, json, os
def run(context):
 app=C.Application.get(); d=F.Design.cast(app.activeProduct); root=d.rootComponent
 out=r'C:\thyristor\deliverables'; m=d.exportManager
 occurrences=list(root.occurrences)
 for occ in occurrences:
  comp=occ.component; name=comp.name
  for f in list(comp.features.extrudeFeatures):
   if name.startswith('01 ') and f.name=='SCR M5 tapped holes': f.isSuppressed=True
   if name.startswith('04 ') and f.name=='Ring bore': f.isSuppressed=True
   if name.startswith('12 ') and 'BShank' in f.name:
    F.DistanceExtentDefinition.cast(f.extentOne).distance.expression='-22 mm'
   if name.startswith('11 ') and 'Shank' in f.name:
    F.DistanceExtentDefinition.cast(f.extentOne).distance.expression='-7 mm'
  if name.startswith(('02 ','03 ','13 ','15 ')):
   mat=occ.transform2; mat.translation=C.Vector3D.create(0,0,0.05); occ.transform2=mat
  if name.startswith('07 '): comp.name='07 SCR baseplate | Generic envelope 68 x 22 x 3.5 mm'
  if name.startswith('08 '): comp.name='08 Thyristor housing | Generic academic envelope'
  if name.startswith('14 '): comp.name='14 Temperature sensor | Illustrative placement; probe detail pending'
 if d.snapshots.hasPendingSnapshot: d.snapshots.add()
 cp=occurrences[0].component
 if not cp.features.extrudeFeatures.itemByName('Reviewed blind mounting bores'):
  pi=cp.constructionPlanes.createInput(); pi.setByOffset(cp.xYConstructionPlane,C.ValueInput.createByReal(1.2))
  plane=cp.constructionPlanes.add(pi); plane.isLightBulbOn=False
  sk=cp.sketches.add(plane)
  for y in (3.2,8.8): sk.sketchCurves.sketchCircles.addByCenterRadius(C.Point3D.create(4,y,0),0.21)
  ps=C.ObjectCollection.create()
  for pr in sk.profiles: ps.add(pr)
  ei=cp.features.extrudeFeatures.createInput(ps,F.FeatureOperations.CutFeatureOperation)
  ei.setOneSideExtent(F.DistanceExtentDefinition.create(C.ValueInput.createByReal(0.4)),F.ExtentDirections.NegativeExtentDirection)
  ei.participantBodies=[b for b in cp.bRepBodies]
  cp.features.extrudeFeatures.add(ei).name='Reviewed blind mounting bores'; sk.isVisible=False
 d.computeAll()
 report={'feature_issues':[],'solid_bodies':0,'components':[]}
 for o in occurrences:
  b=list(o.component.bRepBodies)
  assert all(x.isSolid and x.volume>0 for x in b)
  if o.component.name.startswith('04 '): assert len(b)==1,'Adapter must be one continuous body'
  report['solid_bodies']+=len(b)
  report['components'].append({'name':o.component.name,'bodies':len(b)})
 for t in d.timeline:
  e=t.entity
  if not getattr(e,'isSuppressed',False) and hasattr(e,'healthState') and e.healthState!=F.FeatureHealthStates.HealthyFeatureHealthState:
   report['feature_issues'].append({'feature':e.name,'message':e.errorOrWarningMessage})
 assert not report['feature_issues'],str(report['feature_issues'])
 def image(name,bottom=False):
  vp=app.activeViewport; cam=vp.camera; cam.cameraType=C.CameraTypes.OrthographicCameraType
  cam.target=C.Point3D.create(4,6,1); cam.eye=C.Point3D.create(23,-18,-22 if bottom else 25)
  cam.upVector=C.Vector3D.create(0,0,-1 if bottom else 1); cam.isFitView=True; cam.isSmoothTransition=False
  vp.camera=cam; vp.refresh(); adsk.doEvents(); assert vp.saveAsImageFile(out+'\\'+name,1800,1400)
 image('Reviewed_Assembly.png')
 assert m.execute(m.createFusionArchiveExportOptions(out+'\\Thyristor_Reviewed_Final.f3d'))
 assert m.execute(m.createSTEPExportOptions(out+'\\Thyristor_Reviewed_Final.step'))
 for o in occurrences: o.isLightBulbOn=o.component.name.startswith('01 ')
 image('Reviewed_Internal_Channels.png',True)
 for o in occurrences: o.isLightBulbOn=True
 original=[o.transform2 for o in occurrences]
 for o in occurrences:
  n=o.component.name; dz=0
  if n.startswith('02 '): dz=-1.5
  elif n.startswith(('03 ','13 ','15 ')): dz=-3
  elif n.startswith(('06 ','07 ','08 ','09 ','10 ','11 ')): dz=3
  elif n.startswith(('04 ','05 ')): dz=1
  elif n.startswith('12 '): dz=2
  mat=o.transform2; v=mat.translation; mat.translation=C.Vector3D.create(v.x,v.y,v.z+dz); o.transform2=mat
 if d.snapshots.hasPendingSnapshot: d.snapshots.add()
 image('Reviewed_Exploded.png')
 assert m.execute(m.createFusionArchiveExportOptions(out+'\\Thyristor_Reviewed_Exploded.f3d'))
 for o,mat in zip(occurrences,original): o.transform2=mat
 if d.snapshots.hasPendingSnapshot: d.snapshots.add()
 image('Reviewed_Assembly.png')
 with open(out+'\\Reviewed_Verification.json','w') as f: json.dump(report,f,indent=2)
 print(json.dumps({'success':True,'solids':report['solid_bodies'],'feature_issues':report['feature_issues']}))
'''
c=FusionMCPClient(); r=c.execute_script(SCRIPT)
Path('finish_response.json').write_text(json.dumps(r,indent=2)); print(json.dumps(r))



