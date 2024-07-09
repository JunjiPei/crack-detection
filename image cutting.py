import tkinter as tk
from PIL import Image, ImageTk, ImageOps


class ImageSlicer:
    def __init__(self, root, path):
        self.root = root
        self.root.title("Image Slicer")

        self.start_x = None
        self.start_y = None
        self.rect = None

        self.img = Image.open(path)
        self.tk_img = ImageTk.PhotoImage(self.img)

        # Use Canvas instead of Label
        self.canvas = tk.Canvas(root, width=self.tk_img.width(), height=self.tk_img.height())
        self.canvas.pack()
        self.canvas.create_image(0, 0, image=self.tk_img, anchor='nw')

        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def on_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        # Create a rectangle (initially a point)
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='red')

    def on_drag(self, event):
        # Update the rectangle to follow the mouse
        curX = event.x
        curY = event.y
        self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)

    def on_release(self, event):
        # Define the final rectangle dimensions
        end_x = event.x
        end_y = event.y
        if self.start_x and self.start_y and end_x and end_y:
            self.crop_image(self.start_x, self.start_y, end_x, end_y)

    def crop_image(self, start_x, start_y, end_x, end_y):
        # Crop and save the image based on the rectangle
        box = (start_x, start_y, end_x, end_y)
        cropped_img = self.img.crop(box)
        cropped_img.show()  # Show the cropped image
        cropped_img.save("cropped_image.jpg")  # Save the cropped image


def main():
    root = tk.Tk()
    ImageSlicer(root, "your_image.jpg")
    root.mainloop()


if __name__ == "__main__":
    main()
