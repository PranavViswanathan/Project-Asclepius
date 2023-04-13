
class StudentDetails implements Serializable{
	private String stuName, regno;
	private int math, physics, chemistry, total;
	
	StudentDetails(){
		setStuName("Not Defined");
		setRegno("Not Defined");
		
		setMath(0);
		setPhysics(0);
		setChemistry(0);
	}
	
	StudentDetails (String stuName, String regno, int math, int physics, int chemistry) {
		this.setStuName(stuName);
		this.setRegno(regno);
		this.setMath(math);
		this.setPhysics(physics);
		this.setChemistry(chemistry);
	}

	public String getStuName() {
		return stuName;
	}

	public void setStuName(String stuName) {
		this.stuName = stuName;
	}

	public String getRegno() {
		return regno;
	}

	public void setRegno(String regno) {
		this.regno = regno;
	}

	public int getMath() {
		return math;
	}

	public void setMath(int math) {
		this.math = math;
	}

	public int getPhysics() {
		return physics;
	}

	public void setPhysics(int physics) {
		this.physics = physics;
	}

	public int getChemistry() {
		return chemistry;
	}

	public void setChemistry(int chemistry) {
		this.chemistry = chemistry;
	}
	public int getTotal() {
		total = getMath() + getPhysics() + getChemistry();
		return total;
	}
}

public class Main {
	public static void main(String[] args){
		try {
			StudentDetails stu = new StudentDetails("k", "k", 90,80,90);
			FileOutputStream f = new FileOutputStream("/home/lab21/Desktop/k/JavaOutput/student.txt");
			ObjectOutputStream ob = new ObjectOutputStream(f);
			ob.writeObject(stu);
			ob.flush();
			ob.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
		StudentDetails s = null;
		FileInputStream f;
		try {
			f = new FileInputStream("/home/lab21/Desktop/k/JavaOutput/student.txt");
			ObjectInputStream ob = new ObjectInputStream(f);
			s = (StudentDetails) ob.readObject();
			ob.close();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
		System.out.println(s.getStuName() + " " + s.getRegno() + " " + s.getTotal());		
		
	}

}
