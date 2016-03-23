
IPython notebook



---


Functionality


Basic functionality

  * Pretty way to alternate inline code, inline output (including graphs) and text (markdown) in one document
  * Share the document (```ipynb```) with others and allow them to modify it
  * Export the document to html or pdf to allow "read-only" access
  * Although it is a browser based GUI, it has several key bindings that
> > make working on notebooks much more comfortable and make it a real
> > option for presentations, teaching, etc.

Unexplored features

  * Import of existing scripts
  * Executing/importing notebooks as python files
  * Running public notebooks in a server

Other references and help available on the `online documentation
<http://ipython.org/ipython-doc/dev/interactive/htmlnotebook.html>`_


---


Dependencies


`Main site
<http://ipython.org/ipython-doc/dev/install/install.html#installnotebook>`_

**ZeroMQ & PyZMQ (PyPi)** Tornado (PyPi)
**MathJax: imported automatically if online; for offline use:

> .. sourcecode:: python**

> from IPython.external.mathjax import install\_mathjax
> install\_mathjax()
**Browser compatibility: Safari, Chrome and Firefox**


---


Fire it up


**```ipython notebook```** ```ipython notebook --pylab```
**```ipython notebook --pylab inline```**

Either load up an existing ```ipynb``` or start a new one you can save later.