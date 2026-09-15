import asyncio
import requests
async def function1():
    await asyncio.sleep(5)
    print("function1") 
    

async def function2():
    await asyncio.sleep(3)
    print("function2") 


async def function3():
    await asyncio.sleep(3)
    print("function3") 

# async def main():        #Does task one by one
#      await function1()
#      await function2()
#      await function3()


# async def main2():
#     task1 = asyncio.create_task(function1())  #concurently runs tasks
#     task2 = asyncio.create_task(function2())  #concurently runs tasks
#     task3 = asyncio.create_task(function3())  #concurently runs tasks  
#     await task1
#     await task2
#     await task3

#This is okayy but not prefered as we have to await each task we have a better alternative


async def main3():              #Does the same task but more efficient returns the return valur of each function as well.
    J=await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print(J)
asyncio.run(main3()) 
# asyncio.run(main())


async def download1():
    response=requests.get("https://cdn.pixabay.com/photo/2018/01/14/23/12/nature-3082832_1280.jpg")
    open("4k1.jpg","wb").write(response.content)
    print("Downloaded 1")
    return "downloaded 4k1.jpg"
async def download2():
    response=requests.get("https://wallpapers.com/images/featured/4k-nature-ztbad1qj8vdjqe0p.jpg")
    open("4k2.jpg","wb").write(response.content)
    print("Downloaded 2")
    return "downloaded 4k2.jpg"

async def download3():
    response=requests.get("https://static.vecteezy.com/system/resources/thumbnails/056/506/311/small/a-hyper-realistic-16k-resolutiongraph-of-a-powerful-south-african-lion-roaring-atop-a-sunlit-photo.jpg")
    open("4k3.jpg","wb").write(response.content)
    print("Downloaded 3")
    return "downloaded 4k3.jpg"


async def dmain():             
    i=await asyncio.gather(
        download1(),
        download2(),
        download3(),
    )
    print(i)

asyncio.run(dmain())