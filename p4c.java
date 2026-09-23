import java.io.*;
import java.net.*;
import java.util.*;

class Client {
    static int checksum(String s) {
        int sum = 0;
        for (char c : s.toCharArray()) sum += c;
        return (~sum) & 0xFFFF;
    }

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        Socket s = new Socket("localhost", 5000);
        DataOutputStream out = new DataOutputStream(s.getOutputStream());
        DataInputStream in = new DataInputStream(s.getInputStream());

        System.out.print("Enter data: ");
        String data = sc.nextLine();

        int c = checksum(data);

        out.writeUTF(data);
        out.writeInt(c);

        System.out.println("Checksum sent: " + c);
        System.out.println("Server: " + in.readUTF());

        s.close();
    }
}