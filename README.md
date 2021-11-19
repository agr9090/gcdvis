# gcdvis
A small script to help visualize the euclidean algorithm for computing the greatest common divisor
by tilling a rectangle with the biggest possible squares. The *gcd* will be the side of the smallest
square.
Check [a worked example](https://en.wikipedia.org/wiki/Euclidean_algorithm#Worked_example).

## How to run it

You'll need python and pdflatex. Just type

`python gen.py <a> <b>`

in the command line replacing `<a>` and `<b>` positive integers.
The script will then generate a file named `final.tex` and run pdflatex on it.
If you want the tikz code to use elsewhere just copy from the .tex file. The additional
argument `beamer` will generate a beamer presentation with pauses so that the squares
appear one at a time.

## Example
Running

`python gen.py 21 13`

will generate a pdf with the following image:

![final-1](https://user-images.githubusercontent.com/71186673/142634425-e22bb2ff-cc64-4a75-b250-26f24c68cf3c.png)

While

`python gen.py 21 8 beamer`

generate a beamer presentation with the following content
![final_beamer-1](https://user-images.githubusercontent.com/71186673/142632329-32d70042-6660-4178-a54e-6ee1c6340e1a.png)
![final_beamer-2](https://user-images.githubusercontent.com/71186673/142632330-8ab1a622-9294-4d1a-983a-74f5a296cc4c.png)
![final_beamer-3](https://user-images.githubusercontent.com/71186673/142632333-a56a2767-46dd-4b33-a4f8-72acd89aebb9.png)
![final_beamer-4](https://user-images.githubusercontent.com/71186673/142632335-c7ef25eb-317d-40b6-be65-7ad97b5e54cf.png)
![final_beamer-5](https://user-images.githubusercontent.com/71186673/142632337-64e3e940-72b6-4419-aa08-3be8a4da9575.png)
![final_beamer-6](https://user-images.githubusercontent.com/71186673/142632338-027810d4-5ff9-46fb-9c6c-85ccfea6c85b.png)
![final_beamer-7](https://user-images.githubusercontent.com/71186673/142632341-87bccb82-00a0-41e0-81ab-8493a89dc197.png)
![final_beamer-8](https://user-images.githubusercontent.com/71186673/142632343-ba5778a7-548d-4149-9355-57e98d1ace45.png)
![final_beamer-9](https://user-images.githubusercontent.com/71186673/142632345-38d06e03-e8fd-4d62-81ef-169c11e078e9.png)
