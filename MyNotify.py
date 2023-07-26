#!/usr/bin/python
import notify2
import time
import os 
import argparse


script_dir = os.path.dirname(__file__)
image_dir = os.path.join(script_dir, 'Images')

# Dictionary of default icons from notify2
dialog_icons = {
                'info': 'dialog-information',
                'success': 'dialog-information',
                'warning': 'dialog-warning',
                'error': 'dialog-error'                
                }

# Build icon image from Images location or
# use icons from dialog_icons if the image not found
icons = {}
for icon_item in ('info', 'warning', 'error', 'success'):
    image = os.path.join(image_dir, icon_item + '.png')
    if os.path.exists(image):
        icons[icon_item] = image
    else:
        icons[icon_item] = dialog_icons[icon_item]
    if icon_item == 'error':
        icons['fail'] = icons[icon_item]
        icons['critical'] = icons[icon_item]


def show_notification(app_name="My Notifier", summary="Notification", message="This is test notification",
                      icon="info", urgency=notify2.URGENCY_LOW,
                      timeout=0):
    # Check if the mentioned icon found on dict(icons)
    # If not found check that is image location and 
    # use "info" icons if not found the location
    if icon in icons:
        icon = icons[icon]
    else:        
        if not os.path.exists(icon):
            icon = icons['info']
  
    # Initialize the notify2
    notify2.init(app_name)    
    notifier = notify2.Notification(summary)
    notifier.message = message
    notifier.icon = icon
    # By default the notification closing in 5 secs and 
    # if we set urgency as critical then staying forever and 
    # closing the notification after timeout
    if timeout != 0:
        notifier.set_urgency(notify2.URGENCY_CRITICAL)    
    # Show the notification
    notifier.show()
    if timeout != 0:
        # wait for the timeout
        time.sleep(timeout)
        # closing the notification
        notifier.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Notification program written in Python")
    parser.add_argument('--title', action='store', dest="title", help="Title to display on notification")
    parser.add_argument('--message', action='store', dest='message', help="Message to display in notification")
    parser.add_argument('--icon', action='store', dest='icon', help='Location of ICON image to display')
    parser.add_argument('--timeout', action='store', dest='timeout', help='Timeout for the notification')
    args = parser.parse_args()
    if args.title:
        title = args.title
    else:
        title = "Notification"
    if args.message:
        message = args.message
    else:
        message = "Sample Notification from python notify2"
    if args.icon:
        icon = args.icon
    else:
        icon = 'info'

    if args.timeout:
        timeout = int(args.timeout)
    else:
        timeout = 0

    show_notification(summary=title, message=message, icon=icon, timeout=timeout)

