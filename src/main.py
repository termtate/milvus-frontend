import sys
from PySide6.QtWidgets import QApplication
import qasync
from ui.view import TestWin
from injector import Injector
from qt_material import apply_stylesheet
import asyncio
import functools
from ml.di import RecognizerModule

extra = {
    # Button colors
    'danger': '#dc3545',
    'warning': '#ffc107',
    'success': '#17a2b8',
    # Font
    'font_family': 'Roboto',
    # Density
    'density_scale': '0',
    # Button Shape
    'button_shape': 'default',
}

async def main():
    def close_future(future, loop):
        loop.call_later(10, future.cancel)
        future.cancel()
        
    loop = asyncio.get_event_loop()
    future = asyncio.Future()

    app = QApplication.instance()
    apply_stylesheet(app, "light_blue.xml", extra=extra, invert_secondary=True)

    if hasattr(app, "aboutToQuit"):
        getattr(app, "aboutToQuit").connect(
            functools.partial(close_future, future, loop)
        )

    injector = Injector([RecognizerModule()])
    win = injector.get(TestWin)
    win.show()
    await future
    return True

if __name__ == "__main__":
    try:
        qasync.run(main())
    except asyncio.exceptions.CancelledError:
        sys.exit(0)