import os
from roku import Roku
from colors import Colors

def main():
  print(Colors.GREEN + "Welcome to Sam's Roku Interface!" + Colors.END)
  main_menu()

def main_menu():
  print(Colors.YELLOW + """
    Enter (1) to launch an app.
    Enter (0) to exit.
  """ + Colors.END)
  choice = raw_input(Colors.GREEN + "What would you like to do? " + Colors.END)
  if choice is "1":
    launch_app()
  if choice is "0":
    print("\nGoodbye!")
    exit()  
  else:
    print(Colors.RED + "\nInvalid choice. Please select a valid option." + Colors.END)
    main_menu()  

def launch_app():
  print_apps()
  app_name = raw_input(Colors.GREEN + '\nEnter the name of the app you wish to launch: ' + Colors.END)
  for app in roku.apps:
    if app_name.lower() in app.name.lower():
      print("\nLaunching " + app.name)
      roku[app.id].launch()
      main_menu()
  print(Colors.RED + "\nSorry, we couldn't find that app. Please try again." + Colors.END)
  launch_app()  

def print_apps():
  print(Colors.GREEN + Colors.UNDERLINE + "\nList of available apps:" + Colors.END)
  apps = roku.apps
  if len(apps) % 2 != 0:
    apps.append(" ")
  split = len(apps) / 2
  l1 = apps[0:split]
  l2 = apps[split:]
  for app1, app2 in zip(l1, l2):
    print(Colors.YELLOW + "{0:<30s} \t {1}".format(app1.name.encode('utf-8'), app2.name.encode('utf-8')) + Colors.END)

# Set your Roku IP Address as an environment variable
# using "export ROKU_IP_ADDRESS='YOUR_IP_HERE'"
roku = Roku(os.environ.get('ROKU_IP_ADDRESS'))
# OR: uncomment this line and manually enter your IP
# roku = Roku('YOUR_IP_HERE')
roku.home()

main()
