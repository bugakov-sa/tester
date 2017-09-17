import org.springframework.boot.*;
import org.springframework.boot.autoconfigure.*;
import org.springframework.web.bind.annotation.*;

import java.util.concurrent.*;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.function.Consumer;

class TestResult {
    final boolean isSuccess;
    final String report;

    private TestResult(boolean isSuccess, String report) {
        this.isSuccess = isSuccess;
        this.report = report;
    }

    static TestResult success() {
        return new TestResult(true, "");
    }

    static TestResult failure(String report) {
        return new TestResult(false, report);
    }
}

abstract class TestTask implements Runnable {
    protected final Consumer<TestResult> testResultConsumer;

    private TestTask(Consumer<TestResult> testResultConsumer) {
        this.testResultConsumer = testResultConsumer;
    }

    static TestTask createSleepSuccessStub(Consumer<TestResult> testResultConsumer, long sleepMillis) {
        return new TestTask(testResultConsumer) {
            @Override
            public void run() {
                try {
                    Thread.sleep(sleepMillis);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                testResultConsumer.accept(TestResult.success());
            }
        };
    }
}

@RestController
@EnableAutoConfiguration
public class Tester {

    final ExecutorService executor = Executors.newSingleThreadExecutor();
    final AtomicBoolean isStarted = new AtomicBoolean(false);
    volatile TestResult testResult;

    @GetMapping("/start")
    String start() {
        if(isStarted.compareAndSet(false, true)) {
            executor.execute(TestTask.createSleepSuccessStub(result -> testResult = result, 10000L));
        }
        return "started";
    }

    @GetMapping("/state")
    String getState() {
        if(!isStarted.get()) {
            return "free";
        }
        if(testResult == null) {
            return "work";
        }
        return "finish";
    }

    @GetMapping("/success")
    boolean isSuccess() {
        return testResult != null && testResult.isSuccess;
    }

    @GetMapping("/report")
    String getReport(){
        return (testResult != null) ? testResult.report : "";
    }

    public static void main(String[] args) throws Exception {
        SpringApplication.run(Tester.class, args);
    }
}