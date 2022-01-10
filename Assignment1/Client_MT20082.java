package com.example.sockp;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;

public class Client_MT20082 {
    public static void main(String[] args) {

        String host = "127.0.0.1";
        int port = 5555;

        try(Socket socket = new Socket(host, port)){
            PrintWriter out = new PrintWriter(socket.getOutputStream(),true);
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            Scanner sc = new Scanner(System.in);
            String msg = null;
            while(! "exit".equalsIgnoreCase(msg)){
                msg = sc.nextLine();
                out.println(msg);
                out.flush();
                System.out.println("Server replied " + in.readLine());
            }
            sc.close();
        }catch (IOException e){
            e.printStackTrace();
        }
    }
}
