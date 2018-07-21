package com.enviromusic.graeme.enviromusic;

import android.content.Intent;
import android.os.Bundle;
import android.app.Activity;
import android.util.Log;

public class SearchActivity extends Activity {
    private static final String TAG = "SearchActivity";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_search);

        Log.i(TAG, "Started SearchActivity");

        Intent intent = getIntent();


    }

}
