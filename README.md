# Steganography

With this simple Python file, you can write or read messages within images


# Example

First, run the program:

```
  python3 "file location"
```

After that, type "1" for hide a message and write your message:

```
"Message to hide"
```

Type the path of your image and press ENTER:

```
"Path of the image"
```

Now, our message is hidden in the image, and for see it type 2 and past the path of the image.

```
"Path of the image where the message is hide"
```

Under the path we can see the message we have hidden earlier

# Some additional information

Alls the code work if the image extensione is "JPEG".
If you try to write or read image messages with other extensions (such as PNG), the result is a sequence of numbers, letters and signs

However the message is present at the end but is preceded by all the hex code, resulting in not being very clear.
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

