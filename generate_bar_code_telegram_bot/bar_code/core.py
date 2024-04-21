import io

from PIL import Image
from typing import Optional
import barcode
from barcode.writer import ImageWriter

async def generate_barcode(message:str) -> Optional[io.BytesIO]:
    try:
        writer_options = {
            "write_text": False,
            "background": "white",
            "foreground": "black",
            "module_width": 0.3,
            "module_height": 15,
            "format": "PNG"
        }

        # Create the barcode object with the provided message and writer options
        barcode_obj = barcode.Code128(str(message), writer=ImageWriter())

        # Create a BytesIO buffer to hold the barcode image
        buffer = io.BytesIO()

        # Save the barcode to the buffer
        barcode_obj.write(buffer, options=writer_options)

        # Reset buffer position to the beginning
        buffer.seek(0)

        # Return the buffer containing the barcode image
        return buffer

    except Exception as e:
        print("Error generating QR code: ", e)
        return None

if __name__ == '__main__':
    import asyncio
    message = "https://hrekov.com/"
    res = asyncio.run(generate_barcode(message))
    print(res)
