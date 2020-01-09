import gksu2 as gksu
import gobject
import getpass

def ask_pass_func(context, prompt):
    try:
        return getpass.getpass("Enter root password: ")
    except KeyboardInterrupt:
        print
        err = gobject.GError("keyboard interrupt")
        err.code = gksu.ERROR_CANCELED
        err.domain = "libgksu"
        raise err

ctx = gksu.Context()
ctx.set_command("ls /root")
try:
    gksu.su_full(ctx, ask_pass=ask_pass_func)
except gobject.GError, error:
    if error.code == gksu.ERROR_CANCELED:
        print "Cancel:", error.message
    else:
        print "Error:", error.message
