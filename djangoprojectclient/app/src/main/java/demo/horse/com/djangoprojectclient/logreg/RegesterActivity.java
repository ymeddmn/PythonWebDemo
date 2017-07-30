package demo.horse.com.djangoprojectclient.logreg;

import android.Manifest;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.support.v4.app.ActivityCompat;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;

import com.squareup.okhttp.Call;
import com.squareup.okhttp.Callback;
import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.Response;

import java.io.IOException;
import java.net.URLDecoder;
import java.nio.charset.Charset;

import demo.horse.com.djangoprojectclient.R;


public class RegesterActivity extends AppCompatActivity implements View.OnClickListener {
    private Button btnCode;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_regester);
        initView();
        ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.INTERNET}, 0);
    }

    private void initView() {
        btnCode = (Button) findViewById(R.id.btn_getcode);
        btnCode.setOnClickListener(this);
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, String permissions[], int[] grantResults) {

    }

    @Override
    public void onClick(View v) {
        new Thread(new Runnable() {
            @Override
            public void run() {
                OkHttpClient client = new OkHttpClient();
                FormEncodingBuilder builder = new FormEncodingBuilder();
                builder.add("phone", "13691599815");

                Request request = new Request.Builder()
                        .url("http://192.168.1.100:8000/getCode/")
                        .post(builder.build())
                        .build();
                Call call = client.newCall(request);
                call.enqueue(new Callback() {
                    @Override
                    public void onFailure(Request request, IOException e) {
                        e.printStackTrace();
                    }

                    @Override
                    public void onResponse(Response response) throws IOException {

                        Message msg = handler.obtainMessage();
                        msg.obj = response.body().string();
                        handler.sendMessage(msg);
                    }
                });
            }
        }).start();

    }

    Handler handler = new Handler(new Handler.Callback() {
        @Override
        public boolean handleMessage(Message msg) {
            String m = (String) msg.obj;
            try {
                m = new String(m.getBytes(), Charset.forName("utf-8"));
                m = URLDecoder.decode(m, "utf-8");
                btnCode.setText(m);
            } catch (Exception e) {
                e.printStackTrace();
            }

            return false;
        }
    });
}
