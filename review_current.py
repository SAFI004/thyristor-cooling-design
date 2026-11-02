from mcp_client import FusionMCPClient
import json
from pathlib import Path
c=FusionMCPClient()
script='''import adsk.core as C, adsk.fusion as F, json
app=C.Application.get()
d=F.Design.cast(app.activeProduct)
out={'document':app.activeDocument.name,'components':[],'health':[]}
for occ in d.rootComponent.allOccurrences:
 comp=occ.component
 out['components'].append({'name':comp.name,'visible':occ.isVisible,'bodies':[{'name':b.name,'solid':b.isSolid,'volume':b.volume,'min':b.boundingBox.minPoint.asArray(),'max':b.boundingBox.maxPoint.asArray()} for b in comp.bRepBodies]})
for t in d.timeline:
 e=t.entity
 if hasattr(e,'healthState') and e.healthState!=F.FeatureHealthStates.HealthyFeatureHealthState:
  out['health'].append({'name':e.name,'message':e.errorOrWarningMessage})
print(json.dumps(out))
'''
r=c.execute_script(script,True)
Path('current_review.json').write_text(json.dumps(r,indent=2))
print(json.dumps(r))
