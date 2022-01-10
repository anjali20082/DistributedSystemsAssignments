package com.example.sockp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class MultithreadedServer_MT20082 {
  public static int num = 0;
    public static void main(String[] args) {

        ServerSocket server = null;


        try{
            server = new ServerSocket(5555);
            server.setReuseAddress(true);

            while(true){

                Socket client = server.accept();
                num++;
                System.out.println("New Client " + num  + " Connected");
                HandleCient clientsock = new HandleCient(client, num);

                new Thread(clientsock).start();
            }

        }catch (IOException e){
            e.printStackTrace();
        }finally {
            if(server != null){
                try{
                    server.close();
                }catch (IOException e){
                    e.printStackTrace();
                }
            }
        }
    }

    private  static class HandleCient implements  Runnable{

        private  final Socket clientSock;
        int clientnum;
        public HandleCient(Socket socket, int num){
            this.clientSock = socket;
            this.clientnum = num;
        }

        @Override
        public void run() {

            PrintWriter out = null;
            BufferedReader in = null;
            String message  = "";
            try{
                out = new PrintWriter(clientSock.getOutputStream(),true);
                in = new BufferedReader(new InputStreamReader(clientSock.getInputStream()));

                while((message = in.readLine()) != null){

                    System.out.println( message + " Client " + clientnum  );

                    out.println(message + " client "+ clientnum);

                }
            }catch(IOException e){
                e.printStackTrace();
            }finally{
                try{
                    if(out != null){
                        out.close();
                    }
                    if(in != null)
                        in.close();
                    clientSock.close();
                }catch (IOException e){
                    e.printStackTrace();
                }
            }
        }
    }
}
