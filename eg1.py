import asyncio

async def speak_async():
    print('OMG asynchronicity!')

loop = asyncio.get_event_loop()

'''
The loop.run_until_complete() function is actually blocking, so it won't
return until all of the asynchronous methods are done.
Since we're only running this on a single thread, there is no way
it can move forward while the loop is in progress.
'''
loop.run_until_complete(speak_async())

#loop.run_forever()
loop.close()

#Error -eg1.py:10: RuntimeWarning: coroutine 'speak_async' was never awaited
#speak_async()