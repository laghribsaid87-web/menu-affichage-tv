package com.menutv.app;

import android.annotation.SuppressLint;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.os.Bundle;
import android.text.InputType;
import android.view.KeyEvent;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    
    // ====== METS TON LIEN ICI ======
    private static final String TV_URL = "http://192.168.1.X:8000/viewer.html?project=default"; 
    private static final String SECRET_PIN = "0000"; // Le mot de passe pour quitter
    
    private int backPressCount = 0;
    private long lastBackPressTime = 0;
    
    @SuppressLint("SetJavaScriptEnabled")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        
        // Mode Plein Écran Absolu
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);
        getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
        
        hideSystemUI();

        WebView webView = new WebView(this);
        setContentView(webView);
        
        WebSettings webSettings = webView.getSettings();
        webSettings.setJavaScriptEnabled(true);
        webSettings.setDomStorageEnabled(true);
        webSettings.setMediaPlaybackRequiresUserGesture(false);
        
        webView.setWebViewClient(new WebViewClient());
        webView.loadUrl(TV_URL);
    }
    
    private void hideSystemUI() {
        View decorView = getWindow().getDecorView();
        decorView.setSystemUiVisibility(
                View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY
                | View.SYSTEM_UI_FLAG_LAYOUT_STABLE
                | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
                | View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
                | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
                | View.SYSTEM_UI_FLAG_FULLSCREEN);
    }
    
    @Override
    public boolean onKeyDown(int keyCode, KeyEvent event) {
        if (keyCode == KeyEvent.KEYCODE_BACK) {
            long currentTime = System.currentTimeMillis();
            // Si plus de 2 secondes se sont écoulées, on remet le compteur à 0
            if (currentTime - lastBackPressTime > 2000) {
                backPressCount = 0;
            }
            backPressCount++;
            lastBackPressTime = currentTime;

            if (backPressCount >= 5) {
                backPressCount = 0;
                showExitDialog();
            } else {
                Toast.makeText(this, "Appuyez " + (5 - backPressCount) + " fois pour quitter", Toast.LENGTH_SHORT).show();
            }
            // On bloque le retour normal
            return true;
        }
        return super.onKeyDown(keyCode, event);
    }

    private void showExitDialog() {
        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setTitle("Sécurité Kiosque");
        builder.setMessage("Entrez le code PIN pour quitter l'affichage :");
        
        final EditText input = new EditText(this);
        input.setInputType(InputType.TYPE_CLASS_NUMBER | InputType.TYPE_NUMBER_VARIATION_PASSWORD);
        builder.setView(input);
        
        builder.setPositiveButton("Quitter", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                String pin = input.getText().toString();
                if (pin.equals(SECRET_PIN)) {
                    finish(); // Ferme l'application
                } else {
                    Toast.makeText(MainActivity.this, "Code incorrect !", Toast.LENGTH_LONG).show();
                    hideSystemUI(); // Retour au plein écran
                }
            }
        });
        builder.setNegativeButton("Annuler", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                dialog.cancel();
                hideSystemUI();
            }
        });
        
        builder.show();
    }
}
