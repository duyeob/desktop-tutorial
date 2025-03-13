import java.util.Random;

public class 숫자 {
    public static void main(String[] args) {
        Random rand = new Random();
        int randomNum = rand.nextInt(100); // 0부터 99까지의 랜덤 숫자 생성
        System.out.println("랜덤 숫자: " + randomNum);
    }
}