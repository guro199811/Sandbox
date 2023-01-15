from pydoc import Doc
import speedtest
import pandas as pd

print(dir(speedtest))

df = pd.DataFrame([[10, 20, 30], [100, 200, 300]],
                  columns=['foo', 'bar', 'baz'])
def get_methods(object, spacing=20):
  methodList = []
  for method_name in dir(object):
    try:
        if callable(getattr(object, method_name)):
            methodList.append(str(method_name))
    except Exception:
        methodList.append(str(method_name))
  processFunc = (lambda s: ' '.join(s.split())) or (lambda s: s)
  for method in methodList:
    try:
        print(str(method.ljust(spacing)) + ' ' +
              processFunc(str(getattr(object, method).__doc__)[0:90]))
    except Exception:
        print(method.ljust(spacing) + ' ' + ' getattr() failed')

get_methods(df['foo'])
'''speed = speedtest.speedtest()
download_speed = speed.download()
upload_speed = speed.upload()
print(f'The download speed is {download_speed}')
print(f'The uplaod speed is {upload_speed}')     '''                                     