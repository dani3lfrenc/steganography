
# Steganography

With this simple Python file, you can write or read messages within images


# Example

First, run the program:

![Alt text](/Screenshot/1.png?raw=true)

After that, type "1" for hide a message and write your message:

![Alt text](/Screenshot/2.png?raw=true)

Type the path of your image and press ENTER:

![Alt text](/Screenshot/3.png?raw=true)

Now, our message is hidden in the image, and for see it type 2 and past the path of the image.

![Alt text](/Screenshot/4.png?raw=true)

Under the path we can see the message we have hidden earlier

# Some additional information

All the code work if the image extensione is "JPEG".
If you try to write or read image messages with other extensions (such as PNG), the result is the following:





![Alt text](/Screenshot/img.png?raw=true)

As you can see, the message is present at the end but is preceded by all the hex code, resulting in not being very clear.
I'm working to use this program with all the images extensions.
## Deployment

To deploy this project run

```bash
  python3 "file location"
```


## Authors

- [@dani3lfrenc](https://www.github.com/dani3lfrenc)


## Tech info

**Client:** Made all in python, with no library required

