import asyncio


async def send_email(recipient, delay):
    print(f"Начинаю отправку письма для {recipient}...")
    await asyncio.sleep(delay)
    print(f"Письмо для {recipient} отправлено")


async def main():
    users = [("Alice", 2), ("Bob", 3), ("Charlie", 1), ("Diana", 4)]
    
    tasks = []
    
    for recipient, delay in users:
        task = asyncio.create_task(send_email(recipient, delay))
        tasks.append(task)
    
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())