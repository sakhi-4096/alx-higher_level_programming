#include <Python.h>

/**
 * print_python_list_info - Print information about a Python list
 * @p: Pointer to the Python list object
 *
 * Description: Prints the size, allocated space, and elements of a
 *  list object.
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, alloc, idx;
	const char *type_name = NULL;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);
	for (idx = 0; idx < size; idx++)
	{
		PyObject *item = PyList_GetItem(p, idx);

		type_name = Py_TYPE(item)->tp_name;
		printf("Element %ld: %s\n", idx, type_name);
	}
}
