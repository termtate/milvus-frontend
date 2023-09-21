import sys
from PySide6.QtWidgets import QApplication
import qasync
from ui.view import TestWin
from injector import Injector
from qt_material import apply_stylesheet
import asyncio
import functools
from ml.di import RecognizerModule
from db.di import CollectionModule
from ml.model import Model   # 由于torch模型保存的路径依赖问题，必须要在入口文件导入Model
from common import settings


# https://github.com/CabbageDevelopment/qasync/blob/28c65995497a9b5653547060ccc8b24c56cc5f45/examples/aiohttp_fetch.py#L73C18-L73C18
async def main():
    def close_future(future, loop):
        loop.call_later(10, future.cancel)
        future.cancel()
        
    loop = asyncio.get_event_loop()
    future = asyncio.Future()

    app = QApplication.instance()
    # https://github.com/UN-GCPDS/qt-material/tree/master#themes
    apply_stylesheet(app, "light_blue.xml", extra=settings.THEME_EXTRA, invert_secondary=True)

    if hasattr(app, "aboutToQuit"):
        getattr(app, "aboutToQuit").connect(
            functools.partial(close_future, future, loop)
        )

    # 依赖注入模块injector的入口
    injector = Injector([RecognizerModule(), CollectionModule()])
    win = injector.get(TestWin)
    win.show()
    await future
    return True


if __name__ == "__main__":
    try:
        qasync.run(main())
    except asyncio.exceptions.CancelledError:
        sys.exit(0)