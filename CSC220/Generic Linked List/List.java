/* ***************************************************
 * Meagan Kropp
 * 10/15/2020
 * List.java
 *
 * creates a linked list
 *************************************************** */

// the Node class
class Node<meagan>
{
	private meagan data;
	private Node<meagan> link;

	// constructor
	public Node()
	{
		this.data = null;
		this.link = null;
	}

	// accessor and mutator for the data component
	public meagan getData()
	{
		return this.data;
	}

	public void setData(meagan data)
	{
		this.data = data;
	}

	// accessor and mutator for the link component
	public Node<meagan> getLink()
	{
		return this.link;
	}

	public void setLink(Node<meagan> link)
	{
		this.link = link;
	}
}

// the List class
public class List<meagan>
{
	public static final int MAX_SIZE = 50;

	private Node<meagan> head;
	private Node<meagan> tail;
	private Node<meagan> curr;
	private int num_items;

	// constructor
	// remember that an empty list has a "size" of 0 and its "position" is at -1
	public List()
	{
		head = tail = curr = null;
		num_items = 0;
	}

	// copy constructor
	// clones the list l and sets the last element as the current
	public List(List<meagan> l)
	{
		head = tail = curr = null;
		num_items = 0;
		Node<meagan> temp = l.head;

		while(temp != null)
		{
			this.InsertAfter(temp.getData());
			temp = temp.getLink();
		}
	}

	// navigates to the beginning of the list
	public void First()
	{
		curr = head;
	}

	// navigates to the end of the list
	// the end of the list is at the last valid item in the list
	public void Last()
	{
		curr = tail;
	}

	// navigates to the specified element (0-index)
	// this should not be possible for an empty list
	// this should not be possible for invalid positions
	public void SetPos(int pos)
	{
		if(!IsEmpty() && pos < num_items && pos >= 0)
		{
			curr = head;
			for(int i = 0; i < pos; i ++)
				curr = curr.getLink();
		}	
	}

	// navigates to the previous element
	// this should not be possible for an empty list
	// there should be no wrap-around
	public void Prev()
	{
		if(!IsEmpty())
		{
			Node<meagan> temp = head;
			while (temp.getLink() != curr)
			{
				temp = temp.getLink();
			}
			curr = temp;
		}
	}

	// navigates to the next element
	// this should not be possible for an empty list
	// there should be no wrap-around
	public void Next()
	{
		if(!IsEmpty() && curr != tail)
			curr = curr.getLink();
	}

	// returns the location of the current element (or -1)
	public int GetPos()
	{
		if(IsEmpty())
		{
			return -1;
		}
		
		Node<meagan> temp = head;
		int i = 0;
		while (temp != curr && temp != null)
		{
			i++;
			temp = temp.getLink();
		}
		return i;
	}

	// returns the value of the current element (or -1)
	public meagan GetValue()
	{
		if(curr ==  null)
			return null;
		return curr.getData();
	}

	// returns the size of the list
	// size does not imply capacity
	public int GetSize()
	{
		return (num_items);
	}

	// inserts an item before the current element
	// the new element becomes the current
	// this should not be possible for a full list
	public void InsertBefore(meagan data)
	{
		if(!IsFull())
		{
			if(IsEmpty())
				InsertAfter(data);
			else if(head == curr)
			{
				Node<meagan> n = new Node<meagan>();
				n.setData(data);
				n.setLink(head);
				curr = head = n;
				num_items++;
			}
			else
			{
				Prev();
				InsertAfter(data);
			}
		}			
	}

	// inserts an item after the current element
	// the new element becomes the current
	// this should not be possible for a full list
	public void InsertAfter(meagan data)
	{
		if(!IsFull())
		{
			Node<meagan> n = new Node<meagan>();
			n.setData(data);

			if (IsEmpty())
			{
				head = curr = tail = n;
			}
			else if(curr == tail)
			{
				tail.setLink(n);
				tail = curr = n;
			}
			else
			{
				n.setLink(curr.getLink());
				curr.setLink(n);
				curr = n;
			}
			num_items++; 
		}
	}

	// removes the current element (collapsing the list)
	// this should not be possible for an empty list. If possible,
	// following element becomes new current element.
	public void Remove()
	{
		if(!IsEmpty())
		{
			if(head == curr)
			{
				if (head == tail)
					tail = null;
				head = curr = curr.getLink();
			}
			else if (curr == tail)
			{
				Prev();
				tail = curr;
				tail.setLink(null);
			}
			else
			{
				Prev();
				curr.setLink(curr.getLink().getLink());
				Next();
			}
			num_items--;
		}
	}

	// replaces the value of the current element with the specified value
	// this should not be possible for an empty list
	public void Replace(meagan data)
	{
		if(!IsEmpty())
			curr.setData(data);
	}

	// returns if the list is empty
	public boolean IsEmpty()
	{
		return (num_items == 0);
	}

	// returns if the list is full
	public boolean IsFull()
	{
		return (num_items == MAX_SIZE);		
	}

	// returns if two lists are equal (by value)
	public boolean Equals(List<meagan> l)
	{
		if(this.GetSize() != l.GetSize())
			return false;
		
		Node<meagan> a = head, b = l.head;
		while(a != null && b != null)
		{
			if(a.getData() != b.getData())
				return false;
			a = a.getLink();
			b = b.getLink();
		}
		return true;
	}

	// returns the concatenation of two lists
	// l should not be modified
	// l should be concatenated to the end of *this
	// the returned list should not exceed MAX_SIZE elements
	// the last element of the new list is the current
	public List<meagan> Add(List<meagan> l)
	{
		List<meagan> sum = new List<meagan>(this);
		Node<meagan> temp = l.head;
		while (temp != null)
		{
			sum.InsertAfter(temp.getData());
			temp = temp.getLink();
		}
		return sum;
	}

	// returns a string representation of the entire list (e.g., 1 2 3 4 5)
	// the string "NULL" should be returned for an empty list
	public String toString()
	{
		if(IsEmpty())
		{
			return "NULL";
		}
		String result = "";
		Node<meagan> temp = head;
		while (temp != null)
		{
			result += (temp.getData() + " ");
			temp = temp.getLink();
		}
		return result;
	}
}
