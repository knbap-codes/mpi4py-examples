# mpi4py examples

### This repo contains few examples of mpi usage with Python.

- example1 - vector addition
- example2 - vector norm computation
- example3 - random numbers histogram

### Useful links
- [mpi4py docs](https://mpi4py.readthedocs.io/en/stable/index.html)
- [building MPI](https://mpi4py.readthedocs.io/en/stable/appendix.html#building-mpi)
  
### Requirements
- Python3.3 or above
- MPI library installed 
#### Python virtual environment
```
$ virutalenv path/to/virtualenv_dir
$ source path/to/virtualenv_dir/bin/activate
```
```
$ pip install -r requirements.txt
```
<hr>

## Runnig code

```
$ mpiexec -n <nprocs> python <file_name>.py
```