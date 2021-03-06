package org.tensorflow.yolo.view;

import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.RectF;
import android.util.AttributeSet;
import android.util.TypedValue;
import android.view.View;

import org.tensorflow.yolo.Config;
import org.tensorflow.yolo.model.BoxPosition;
import org.tensorflow.yolo.model.Recognition;
import org.tensorflow.yolo.util.ClassAttrProvider;

import java.util.LinkedList;
import java.util.List;

/**
 * A simple View providing a render callback to other classes.
 * Modified by Zoltan Szabo
 */
public class OverlayView extends View {
    private final Paint paint;
    private final List<DrawCallback> callbacks = new LinkedList();
    private List<Recognition> results;
    private List<Integer> colors;
    private float resultsViewHeight;

    public OverlayView(final Context context, final AttributeSet attrs) {
        super(context, attrs);
        paint = new Paint();
        paint.setColor(Color.GREEN);
        paint.setStyle(Paint.Style.STROKE);
        paint.setTextSize(TypedValue.applyDimension(TypedValue.COMPLEX_UNIT_DIP,
                15 * 2, getResources().getDisplayMetrics()));       // shimatani
        resultsViewHeight = TypedValue.applyDimension(TypedValue.COMPLEX_UNIT_DIP,
                112, getResources().getDisplayMetrics());
        colors = ClassAttrProvider.newInstance(context.getAssets()).getColors();
    }

    public void addCallback(final DrawCallback callback) {
        callbacks.add(callback);
    }

    @Override
    public synchronized void onDraw(final Canvas canvas) {
        for (final DrawCallback callback : callbacks) {
            callback.drawCallback(canvas);
        }
        float stW = paint.getStrokeWidth();     // shimatani

        if (results != null) {
            for (int i = 0; i < results.size(); i++) {
                RectF box = reCalcSize(results.get(i).getLocation());
                String title = results.get(i).getTitle()
                        + ":"
                        + String.format("%.2f", results.get(i).getConfidence());
                paint.setColor(colors.get(results.get(i).getId()));
                paint.setStrokeWidth(8);                 // shimatani
                canvas.drawRect(box, paint);
                paint.setStrokeWidth(stW);               // shimatani
                canvas.drawText(title, box.left, box.top - 100, paint);   // shimatani

                // shimatani
                Integer garbageNum = garbageSeparate(i);
                String garbage = "ごみ箱"
//                      + String.format("%2d", results.get(i).getId())
                        + String.format("%2d", garbageNum)
                        + "番へ";
                canvas.drawText(garbage, box.left, box.top, paint);
            }
        }
    }

    private Integer garbageSeparate(int i) {
        Integer garbageNum = results.get(i).getId();
        switch(garbageNum){
            case 0:
                garbageNum = 19;    // Ｃ型リモコン
                break;
            case 1:
                garbageNum = 7;    // 軍手・革手
                break;
            case 2:
                garbageNum = 13;    //マーカー
                break;
            case 3:
                garbageNum = 19;     // Ｇ型リモコン
                break;
            case 4:
                garbageNum = 19;     // Ｅ型リモコン
                break;
            case 5:
                garbageNum = 23;     // ボタン電池
                break;
            case 6:
                garbageNum = 23;     // 乾電池
                break;
            case 7:
                garbageNum = 10;    // タイラップ
                break;
            case 8:
                garbageNum = 9;    // ＰＰバンド
                break;
            default:
                garbageNum = 99;    // 未分類
                break;
        }
        return garbageNum;
    }

    public void setResults(final List<Recognition> results) {
        this.results = results;
        postInvalidate();
    }

    /**
     * Interface defining the callback for client classes.
     */
    public interface DrawCallback {
        void drawCallback(final Canvas canvas);
    }

    private RectF reCalcSize(BoxPosition rect) {
        int padding = 5;
        float overlayViewHeight = this.getHeight() - resultsViewHeight;
        float sizeMultiplier = Math.min((float) this.getWidth() / (float) Config.INPUT_SIZE,
                overlayViewHeight / (float) Config.INPUT_SIZE);

        float offsetX = (this.getWidth() - Config.INPUT_SIZE * sizeMultiplier) / 2;
        float offsetY = (overlayViewHeight - Config.INPUT_SIZE * sizeMultiplier) / 2 + resultsViewHeight;

        float left = Math.max(padding,sizeMultiplier * rect.getLeft() + offsetX);
        float top = Math.max(offsetY + padding, sizeMultiplier * rect.getTop() + offsetY);

        float right = Math.min(rect.getRight() * sizeMultiplier, this.getWidth() - padding);
        float bottom = Math.min(rect.getBottom() * sizeMultiplier + offsetY, this.getHeight() - padding);

        return new RectF(left, top, right, bottom);
    }
}
