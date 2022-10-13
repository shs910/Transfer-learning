from itertools import count
import numpy as np
import json

count={'entailment':0,'neutral':0,'contradiction':0}
with open('entailment.json','w+') as f1:
    with open('neutral.json','w+') as f2:
        with open('contradiction.json','w+') as f3:
            with open('train.50k.json','r',encoding='utf-8') as f:
                for line in f.readlines():
                    d=json.loads(line)
                    samp=dict()
                    samp['sentence1']=d['sentence1']
                    samp['sentence2']=d['sentence2']
                    samp['label']=d['label']
                    if d['label']=='entailment':
                        #f1.write(json.dumps(samp, ensure_ascii=False)+'\n')
                        count['entailment']+=1
                    elif d['label']=='neutral':
                        #f2.write(json.dumps(samp, ensure_ascii=False)+'\n')
                        count['neutral']+=1
                    elif d['label']=='contradiction': 
                        #f3.write(json.dumps(samp, ensure_ascii=False)+'\n')
                        count['contradiction']+=1
            f.close()
        f3.close()
    f2.close()
f1.close()
print(count)