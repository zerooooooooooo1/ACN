import java.io.*;
import java.net.*;

class Server {
    static int checksum(String s) {
        int sum = 0;
        for (char c : s.toCharArray()) sum += c;
        return (~sum) & 0xFFFF;
    }

    public static void main(String[] args) throws Exception {
        ServerSocket ss = new ServerSocket(5000);
        System.out.println("Server waiting...");

        Socket s = ss.accept();
        DataInputStream in = new DataInputStream(s.getInputStream());
        DataOutputStream out = new DataOutputStream(s.getOutputStream());

        String data = in.readUTF();
        int received = in.readInt();
        int calculated = checksum(data);

        System.out.println("Received data: " + data);
        System.out.println("Received checksum: " + received);
        System.out.println("Calculated checksum: " + calculated);

        if (received == calculated)
            out.writeUTF("Data is correct - Checksum verified");
        else
            out.writeUTF("Data is corrupted - Checksum failed");

        s.close();
        ss.close();
    }
}