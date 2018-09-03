package org.tensorflow.yolo.view;

import android.graphics.Bitmap;
import android.graphics.Bitmap.Config;
import android.graphics.Canvas;
import android.graphics.Matrix;
import android.graphics.Typeface;
import android.media.Image;
import android.media.ImageReader;
import android.media.ImageReader.OnImageAvailableListener;
import android.os.SystemClock;
// import android.speech.tts.TextToSpeech;
import android.util.Log;
import android.util.Size;
import android.util.TypedValue;

import org.tensorflow.yolo.R;
import org.tensorflow.yolo.TensorFlowImageRecognizer;
import org.tensorflow.yolo.model.Recognition;
import org.tensorflow.yolo.util.ImageUtils;
import org.tensorflow.yolo.view.components.BorderedText;

import java.util.List;
import java.util.Vector;

import static org.tensorflow.yolo.Config.INPUT_SIZE;
import static org.tensorflow.yolo.Config.LOGGING_TAG;

/**
 * Classifier activity class
 * Modified by Zoltan Szabo
 */
public class ClassifierActivity extends TextToSpeechActivity implements OnImageAvailableListener {
    private boolean MAINTAIN_ASPECT = true;
    private float TEXT_SIZE_DIP = 10;

    private TensorFlowImageRecognizer recognizer;
    private Integer sensorOrientation;
    private int previewWidth = 0;
    private int previewHeight = 0;
    private Bitmap croppedBitmap = null;
    private boolean computing = false;
    private Matrix frameToCropTransform;

    private OverlayView overlayView;
    private BorderedText borderedText;
    private long lastProcessingTimeMs;

    private String lastRecognizedClass = "";    // shimatani
    // private TextToSpeech tts;   // shimatani

    @Override
    public void onPreviewSizeChosen(final Size size, final int rotation) {
        final float textSizePx = TypedValue.applyDimension(TypedValue.COMPLEX_UNIT_DIP,
                TEXT_SIZE_DIP, getResources().getDisplayMetrics());
        borderedText = new BorderedText(textSizePx * 2);    // shimatani
        borderedText.setTypeface(Typeface.MONOSPACE);

        recognizer = TensorFlowImageRecognizer.create(getAssets());

        overlayView = (OverlayView) findViewById(R.id.overlay);
        previewWidth = size.getWidth();
        previewHeight = size.getHeight();

        final int screenOrientation = getWindowManager().getDefaultDisplay().getRotation();

        Log.i(LOGGING_TAG, String.format("Sensor orientation: %d, Screen orientation: %d",
                rotation, screenOrientation));

        sensorOrientation = rotation + screenOrientation;

        Log.i(LOGGING_TAG, String.format("Initializing at size %dx%d", previewWidth, previewHeight));

        croppedBitmap = Bitmap.createBitmap(INPUT_SIZE, INPUT_SIZE, Config.ARGB_8888);

        frameToCropTransform = ImageUtils.getTransformationMatrix(previewWidth, previewHeight,
                INPUT_SIZE, INPUT_SIZE, sensorOrientation, MAINTAIN_ASPECT);
        frameToCropTransform.invert(new Matrix());

        addCallback((final Canvas canvas) -> renderAdditionalInformation(canvas));
    }

    @Override
    public void onImageAvailable(final ImageReader reader) {
        Image image = null;

        try {
            image = reader.acquireLatestImage();

            if (image == null) {
                return;
            }

            if (computing) {
                image.close();
                return;
            }

            computing = true;
            fillCroppedBitmap(image);
            image.close();
        } catch (final Exception ex) {
            if (image != null) {
                image.close();
            }
            Log.e(LOGGING_TAG, ex.getMessage());
        }

// shimatani
        String tts = makeTts();
        Log.i(LOGGING_TAG, tts);

        runInBackground(() -> {
            final long startTime = SystemClock.uptimeMillis();
            final List<Recognition> results = recognizer.recognizeImage(croppedBitmap);
            lastProcessingTimeMs = SystemClock.uptimeMillis() - startTime;
            if (!(results.isEmpty() || lastRecognizedClass.equals(results.get(0).getTitle()))) {
                lastRecognizedClass = results.get(0).getTitle();    // shimatani
            }
            overlayView.setResults(results);

// shimatani
            // speak(results);
            speak2(results, tts);

            requestRender();
            computing = false;
        });
    }

    private String makeTts() {
        String info1 = "";
        String info2 = "";
        String tts = "";
        switch (lastRecognizedClass) {
            case "乾電池":
                info1 = "乾電池は23番です";
                break;
            case "粘着テープ":
                info1 = "粘着テープの場合、紙は2番、";
                info2 = "布/養生は12番、ビニールは13番です";
                break;
            case "ボタン電池":
                info1 = "水銀を含まないボタン電池は23番です";
                break;
            default:
                break;
        }
        tts = info1 + info2;
        return tts;
    }

    private void fillCroppedBitmap(final Image image) {
            Bitmap rgbFrameBitmap = Bitmap.createBitmap(previewWidth, previewHeight, Config.ARGB_8888);
            rgbFrameBitmap.setPixels(ImageUtils.convertYUVToARGB(image, previewWidth, previewHeight),
                    0, previewWidth, 0, 0, previewWidth, previewHeight);
            new Canvas(croppedBitmap).drawBitmap(rgbFrameBitmap, frameToCropTransform, null);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (recognizer != null) {
            recognizer.close();
        }
    }

    private void renderAdditionalInformation(final Canvas canvas) {
        final Vector<String> lines = new Vector();

        if (recognizer != null) {
            for (String line : recognizer.getStatString().split("\n")) {
                lines.add(line);
            }
        }

// shimatani
        // lines.add("Frame: " + previewWidth + "x" + previewHeight);
        // lines.add("View: " + canvas.getWidth() + "x" + canvas.getHeight());
        // lines.add("Rotation: " + sensorOrientation);
        // lines.add("Inference time: " + lastProcessingTimeMs + "ms");

        Log.i(LOGGING_TAG, "検出名");
        lines.add("検出名: " + lastRecognizedClass);

        String info1 = "";
        String info2 = "";
        switch(lastRecognizedClass){
            case "乾電池":
                info1 = "乾電池は23番です";
                break;
            case "粘着テープ":
                info1 = "粘着テープの場合、紙は2番、";
                info2 = "布/養生は12番、ビニールは13番です";
                break;
            case "ボタン電池":
                info1 = "水銀を含まないボタン電池は23番です";
                break;
            default:
                break;
        }
        lines.add(info1);
        lines.add(info2);

        borderedText.drawLines(canvas, 10, 10, lines);
    }
}
