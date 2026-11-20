# A game-based update loop,
# modeled after UnityEngine's runtime execution
# 
# Made by CalmBubbles
# 
# This does not follow the standard naming conventions of py lollll 


import threading
import time
import asyncio


class __Loop:
    class __Call:
        callback = None
        clear = False
        timeout = 1
        time = 1

    __shouldEnd = False
    __callUpdate = False
    __startTime = 0
    __frameIndex = 0
    __uTime = 0
    __uDeltaTime = 0
    __time = 0
    __deltaTime = 0
    __calls = []

    __updateThread = None

    targetFrameRate: int = -1
    timeScale: float = 1
    maximumDeltaTime: float = 0.1111111

    frameCount: int = property(lambda self: self.__frameIndex)
    unscaledTime: float = property(lambda self: self.__uTime)
    unscaledDeltaTime: float = property(lambda self: self.__uDeltaTime)
    time: float = property(lambda self: self.__time)
    deltaTime: float = property(lambda self: self.__deltaTime)

    def __RequestUpdate (self): 
        while not self.__shouldEnd: self.__Update()

    def __UpdateBase (self):
        self.__uDeltaTime = (time.perf_counter() - self.__startTime) - self.__uTime
        self.__uTime += self.__uDeltaTime

        deltaT = self.__uDeltaTime

        if deltaT > self.maximumDeltaTime: deltaT = self.maximumDeltaTime

        self.__deltaTime = deltaT * self.timeScale
        self.__time += self.__deltaTime

        self.__frameIndex += 1

        self.__callUpdate = True

    def __Update (self):
        if self.targetFrameRate > 0:
            slice = (1 / self.targetFrameRate)
            accumulator = (time.perf_counter() - self.__startTime) - self.__uTime

            while (accumulator >= slice):
                self.__UpdateBase()
                accumulator -= slice
        else: self.__UpdateBase()

        if not self.__callUpdate: return

        removingCalls = []

        for i in range(len(self.__calls)):
            call = self.__calls[i]

            call.time += self.__deltaTime

            if (call.time <= call.timeout): continue

            call.callback()

            if (call.clear()): removingCalls.append(call)
            else: call.time = 0

        for i in range(len(removingCalls)): self.__calls.remove(removingCalls[i])
        
        self.__callUpdate = False
    
    def Append (self, callback: function, delay: float = 0, shouldClear: function[bool] = (lambda: False)):
        call = self.__Call()
        call.callback = callback
        call.clear = shouldClear
        call.timeout = delay

        self.__calls.append(call)

    async def Delay (self, time: float):
        if time < self.__deltaTime: return
        
        done = False
        loop = asyncio.get_running_loop()
        future = loop.create_future()

        def check ():
            nonlocal done

            done = True
            loop.call_soon_threadsafe(future.set_result, 0)

        self.Append(check, time, lambda: done)

        await future

    async def Wait (self, conditionCall: function[bool]):
        loop = asyncio.get_running_loop()
        future = loop.create_future()

        def waitLoop ():
            while not conditionCall(): pass
            loop.call_soon_threadsafe(future.set_result, 0)
        
        thread = threading.Thread(target = waitLoop)
        thread.daemon = True
        thread.run()

        await future
    
    def Start (self):
        self.__startTime = time.perf_counter()

        self.__updateThread = threading.Thread(target = self.__RequestUpdate)
        self.__updateThread.start()
    
    def End (self): self.__shouldEnd = True

Loop = __Loop()