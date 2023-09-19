# from ppocr import PPOcr
# from ml.di import RecognizerModule
# from injector import Injector

# i = Injector([RecognizerModule()])
# ocr = i.get(PPOcr)

# r = ocr.run(r"C:\Users\DEL\Desktop\a.png")

# print(r)

import asyncio

async def a():
    await asyncio.sleep(2)
    print("a1")
    await asyncio.sleep(2)
    print("a1")


async def b():
    await asyncio.sleep(3)
    print("b")
    
async def main():
    print("----")
    await asyncio.gather(a(), b())
    print("----")

asyncio.run(main())