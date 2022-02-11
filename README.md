# Fractal Generation
 A project created to explore fractals and how they're generated. 
 
 The core fractal that was explored was the classic [Mandelbrot](https://en.wikipedia.org/wiki/Mandelbrot_set), as well as the [Burning Ship](https://en.wikipedia.org/wiki/Burning_Ship_fractal) fractal. Finally a modified fractal generation function is included to create associated [Julia sets](https://en.wikipedia.org/wiki/Julia_set). These fractals are very interesting since they are self similar (you can find copies of it within itself) and they have infinite detail (you can zoom infinitley), the only restriction is how long you want to wait for your computer to finish.
 

## Here are some generated images:

A simple Mandelbrot fractal, one of the most common fractals. It's created based in taking the pixel offset from a defined center, and squaring the corresponding complex value iterativley. Black regions represent convergent sequences, while lighter regions represent divergent sequences. We can also use the speed of the divergence itself to color the fractal in interesting ways.

<img src="/pics/mandlebrot.png" width="400">

The Multibrot fractal. The Mandelbrot fractal is actually a special case of the multibrot where the complex power equals 2. Modifying this power gives us some much more chaotic and weird results.

<img src="/pics/multibrot.png" width="400">

One of the Mandelbrot's associated Julia sets. Created by modifying how we use our pixel position as complex function inputs. This julia set is considered to be "unstable" because small changes to the input parameters can drastically change the finished image.

<img src="/pics/JuliaSet_processed.png" width="400" style="transform:rotate(90deg)">


