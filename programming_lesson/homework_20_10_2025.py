import asyncio
import random
import time

meals = {'steak': 7, 'pasta': 5, 'soup': 3}
salads = {'caesar': 4, 'greek': 2, 'olivier': 6}
desserts = {'cake': 5, 'icecream': 2}

def randomized_time(base: int) -> float:

    delta = random.uniform(-2, 2)
    t = base + delta
    return max(0.5, round(t, 2))

async def prepare_and_wait(name: str, base_time: int, main_ready_event: asyncio.Event,
                           is_main: bool=False, is_salad: bool=False, is_dessert: bool=False):

    prep_time = randomized_time(base_time)
    start = time.perf_counter()
    print(f"{name} is being prepared ({prep_time}s)")
    await asyncio.sleep(prep_time)
    elapsed = round(time.perf_counter() - start, 2)

    if is_main:
        print(f"{name} is ready! (prepared in {elapsed}s)")
        main_ready_event.set()
        print(f"Serving {name} and any waiting salad(s)...")
    else:
        if not main_ready_event.is_set():
            if is_dessert:
                print(f"{name} is ready, but waiting for main dish...")
            elif is_salad:
                print(f"{name} is ready, waiting for main dish...")
            await main_ready_event.wait()

        print(f"Serving {name}... (prepared in {elapsed}s)")

async def main():
    main_choice = input("Choose main meal: ").strip().lower()
    salad_choice = input("Choose salad: ").strip().lower()
    dessert_choice = input("Choose dessert: ").strip().lower()

    if main_choice not in meals:
        print(f"Unknown main meal '{main_choice}'. Available: {', '.join(meals)}")
        return
    if salad_choice not in salads:
        print(f"Unknown salad '{salad_choice}'. Available: {', '.join(salads)}")
        return
    if dessert_choice not in desserts:
        print(f"Unknown dessert '{dessert_choice}'. Available: {', '.join(desserts)}")
        return

    main_ready_event = asyncio.Event()

    tasks = [
        asyncio.create_task(prepare_and_wait(main_choice, meals[main_choice], main_ready_event,
                                            is_main=True)),
        asyncio.create_task(prepare_and_wait(salad_choice, salads[salad_choice], main_ready_event,
                                            is_salad=True)),
        asyncio.create_task(prepare_and_wait(dessert_choice, desserts[dessert_choice], main_ready_event,
                                            is_dessert=True)),
    ]


    await asyncio.gather(*tasks)

    print("All dishes are served!")

if __name__ == "__main__":

    asyncio.run(main())

