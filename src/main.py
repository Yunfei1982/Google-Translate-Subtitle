from pathlib import Path
import pysrt
from googletrans import Translator

dir_path = '/Users/yunfei/Movies/Learning Serum'
src_lang = 'en'
target_lang = 'zh-CN'
translator = Translator(service_urls=['translate.google.cn'])

p = Path(dir_path)
srt_files = sorted(list(p.glob('**/*.srt')))

for f in srt_files:
    print(f'translate {f} ......')
    subtitles = pysrt.open(f)
    translate_result = translator.translate(subtitles.text,src = src_lang, dest = target_lang).text.split('\n')
    
    for i in range(len(subtitles)):
        subtitles[i].text = translate_result[i]
        
    new_filename = f.with_name(f'{f.stem}.{target_lang}{f.suffix}')
    subtitles.save(new_filename)
    print(f'save new srt file to: {new_filename}')

print('finished...')
