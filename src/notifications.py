import gi


def show_notification():
    # Create a Gio.Notification
    notification = Gio.Notification()
    notification.set_title("Sample Notification")
    notification.set_body("This is a sample notification!")

    # Display the notification
    Gio.Notification.set_priority(notification, Gio.NotificationPriority.NORMAL)
    Gio.Notification.set_default_action(notification, "app.open")

    # Create a Gio.Application to handle the default action
    app = Gio.Application.get_default()
    if not app:
        app = Gio.Application.new("org.example.notification", Gio.ApplicationFlags.FLAGS_NONE)
        app.connect("activate", lambda app: print("Application activated"))
        app.connect("open", lambda app, files, hint: print("Notification default action clicked"))
        app.register(None)

    # Send the notification
    app.send_notification(None, notification)

