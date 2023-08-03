import sys
from PySide6.QtWidgets import QApplication
import qasync
from ui.view import TestWin
from injector import Injector
from qt_material import apply_stylesheet
import asyncio
import functools
from ml.di import PaddleOCRModule

async def main():
    def close_future(future, loop):
        loop.call_later(10, future.cancel)
        future.cancel()
        
    loop = asyncio.get_event_loop()
    future = asyncio.Future()

    app = QApplication.instance()
    apply_stylesheet(app, "light_blue.xml", invert_secondary=True)
    if hasattr(app, "aboutToQuit"):
        getattr(app, "aboutToQuit").connect(
            functools.partial(close_future, future, loop)
        )

    injector = Injector([PaddleOCRModule()])
    win = injector.get(TestWin)
    win.show()

    await future
    return True

if __name__ == "__main__":
    try:
        qasync.run(main())
    except asyncio.exceptions.CancelledError:
        sys.exit(0)