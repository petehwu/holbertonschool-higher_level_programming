#include <stdio.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t thesize = PyList_Size(p);
	Py_ssize_t themem = ((PyListObject *) p)->allocated;
	Py_ssize_t count = 0;

	printf("[*] Size of the Python List = %ld\n", thesize);
	printf("[*] Allocated = %ld\n", themem);
	while (count < thesize)
	{
		printf("Element %ld: %s\n", count,
				Py_TYPE((PyList_GetItem(p, count)))->tp_name);
		count++;
	}

}
