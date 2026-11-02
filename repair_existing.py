from mcp_client import FusionMCPClient
from pathlib import Path
import json
SCRIPT = r'''
import adsk, adsk.core as C, adsk.fusion as F, json, os
def run(context):
 app=C.Application.get(); d=F.Design.cast(app.activeProduct); root=d.rootComponent
 out=r'C:\thyristor\deliverables'; m=d.exportManager
 assert m.execute(m.createFusionArchiveExportOptions(out+'\\Before_Review_Backup.f3d'))
 report={'repairs':[],'features':[]}
 for occ in root.occurrences:
  comp=occ.component
  for feature in comp.features.extrudeFeatures:
   report['features'].append({'component':comp.name,'name':feature.name})
   if 'Ring bore' in feature.name:
    feature.timelineObject.rollTo(True)
    feature.participantBodies=[b for b in comp.bRepBodies]
    d.timeline.moveToEnd()
    report['repairs'].append('Restricted '+comp.name+' bore to its own body')
   if 'SCR M5 tapped holes' in feature.name:
    extent=F.DistanceExtentDefinition.cast(feature.extentOne)
    extent.distance.expression='4 mm'
    report['repairs'].append('SCR blind pilot holes reduced to 4 mm; threads conceptual')
 d.computeAll()
 report['components']=[{'name':o.component.name,'bodies':o.component.bRepBodies.count} for o in root.occurrences]
 with open(out+'\\review_repair_stage.json','w') as f: json.dump(report,f,indent=2)
 print(json.dumps(report))
'''
c=FusionMCPClient()
r=c.execute_script(SCRIPT)
Path('repair_response.json').write_text(json.dumps(r,indent=2))
print(json.dumps(r))

