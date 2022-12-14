import asyncio
from genusers.smsactivator.activator_main import activator_main


def main():
    current_number = activator_main()


#def async_run():
#    asyncio.run(main())