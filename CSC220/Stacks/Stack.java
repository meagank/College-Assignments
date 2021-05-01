/* ***************************************************
 * Meagan Kropp
 * 10/28/2020
 * Stack.java
 *
 * creates a stack with generics and uses methods from List.java
 *************************************************** */


class Stack<meagan>
{
	private List<meagan> list;
		
	public Stack()

		list = new List<meagan>();
	}

	public Stack(Stack<meagan> s)
	{
		list = new List<meagan>(s.list);
	}
	
	public void Push(meagan data)
	{
		list.First();
		list.InsertBefore(data);
	}

	public meagan Pop()
	{
		list.First();
		meagan data = list.GetValue();
		list.Remove();
		return data;
	}

	public meagan Peek()
	{
		list.First();
		return list.GetValue();
	}

	public int Size()
	{
		return list.GetSize();
	}

	public boolean IsEmpty()
	{
		return list.IsEmpty();
	}

	public boolean IsFull()
	{
		return list.IsFull();
	}

	public boolean Equals(Stack<meagan> s)
	{
		return (list.Equals(s.list));
	}

	public Stack<meagan> Add(Stack<meagan> s)
	{
		Stack<meagan> newStack = new Stack<meagan>(this);
		newStack.list = newStack.list.Add(s.list);
		return newStack;
	}

	public String toString()
	{
		return list.toString();
	}
	
}

