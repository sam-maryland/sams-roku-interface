import os
from roku import Roku
from keyboard import press
from getch import getch
from colors import Colors

# Set your Roku IP Address as an environment variable
# by running "export ROKU_IP_ADDRESS='YOUR_IP_HERE'"
# from the command line
roku = Roku(os.environ.get('ROKU_IP_ADDRESS'))

def main():
  print(Colors.GREEN + "Welcome to Sam's Roku Interface!" + Colors.END)
  main_menu()

def main_menu():
  print(Colors.GREEN + Colors.UNDERLINE + "\nMain Menu:" + Colors.END)
  print(Colors.YELLOW + """  
    Enter (1) to launch an app.
    Enter (2) to see what app is currently running.
    Enter (3) to close the current app.
    Enter (4) to enter controller mode.
    Enter (0) to exit.
  """ + Colors.END)
  choice = raw_input(Colors.GREEN + "What would you like to do? " + Colors.END)
  if choice is "1":
    launch_app()
  if choice is "2":
    current_app()
  if choice is "3":
    close_current_app()
  if choice is "4":
    controller_mode()  
  if choice is "0":
    print("\nGoodbye!")
    exit()  
  else:
    print(Colors.RED + "\nInvalid choice. Please select a valid option." + Colors.END)
    main_menu()  

def launch_app():
  print_apps()
  app_name = raw_input(Colors.GREEN + "\nEnter the name of the app you wish to launch: " + Colors.END)
  for app in roku.apps:
    if app_name.lower() in app.name.lower():
      roku.home()
      print(Colors.GREEN + "\nLaunching " + app.name + "..." + Colors.END)
      roku[app.id].launch()
      main_menu()
  print(Colors.RED + "\nSorry, we couldn't find that app. Please try again." + Colors.END)
  launch_app()  

def current_app():
  print(Colors.RED + "\nThe current app running is: " + roku.active_app.name + Colors.END)  
  main_menu() 

def close_current_app():
  print(Colors.RED + "\nClosing the current app..." + Colors.END)
  roku.home()  
  main_menu()

def controller_mode():
  print(Colors.YELLOW + """
    Power        - (P)
    Back         - (Backspace)
    Home         - (H)
    Play/Pause   - (Space)
    Fast Forward - (K)
    Rewind       - (J)
    Volume Up    - (+)
    Volume Down  - (-)
    Mute         - (0)
    Select       - (Enter)
    Use WASD to control.
    Press ESC to return to the menu.
  """ + Colors.END)  
  active = True
  while active:
    try: 
      action = ord(getch())
      if action is 112:
        roku.power()
      elif action is 127:
        roku.back()
      elif action is 104:
        roku.home()  
      elif action is 32:
        roku.play()
      elif action is 107:
        roku.forward()
      elif action is 106:
        roku.reverse() 
      elif action is 61:
        roku.volume_up()
      elif action is 45:
        roku.volume_down() 
      elif action is 48:
        roku.volume_mute()        
      elif action is 13:
        roku.select()
      elif action is 119:
        roku.up()
      elif action is 97:
        roku.left() 
      elif action is 115:
        roku.down()   
      elif action is 100:
        roku.right()         
      elif action is 27:
        active = False
      else:
        print(Colors.RED + "\nPlease select a valid option." + Colors.END)
    except:
      print(Colors.RED + "\nSorry, your device does not support this functionality." + Colors.END)
  main_menu()  

def print_apps():
  print(Colors.GREEN + Colors.UNDERLINE + "\nList of available apps:\n" + Colors.END)
  apps = roku.apps
  if len(apps) % 2 != 0:
    apps.append(" ")
  split = len(apps) / 2
  l1 = apps[0:split]
  l2 = apps[split:]
  for app1, app2 in zip(l1, l2):
    if hasattr(app1, 'name') and hasattr(app2, 'name'):
      print(Colors.YELLOW + "\t{0:<30s} \t {1}".format(app1.name.encode('utf-8'), app2.name.encode('utf-8')) + Colors.END)

main()
