/* ***************************************************
 * Meagan Kropp
 * 10/28/2020
 * Queue.java
 *
 * creates a queue with generics and uses methods from List.java
 *************************************************** */


class Queue<meagan>
{
	private List<meagan> list;
		
	public Queue()
	{
		list = new List<meagan>();
	}

	public Queue(Queue<meagan> s)
	{
		list = new List<meagan>(s.list);
	}
	
	public void Enqueue(meagan data)
	{
		list.Last();
		list.InsertAfter(data);
	}

	public meagan Dequeue()
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

	public boolean Equals(Queue<meagan> s)
	{
		return (list.Equals(s.list));
	}

	public Queue<meagan> Add(Queue<meagan> s)
	{
		Queue<meagan> newQueue = new Queue<meagan>(this);
		newQueue.list = newQueue.list.Add(s.list);
		return newQueue;
	}

	public String toString()
	{
		return list.toString();
	}
	
}