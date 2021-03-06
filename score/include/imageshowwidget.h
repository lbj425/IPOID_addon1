#ifndef IMAGESHOWWIDGET_H
#define IMAGESHOWWIDGET_H
#include "eyetrackerwrapper.h"
#include "myconfig.h"
#include "mytypedef.h"
#include "scorepage.h"
#include <QLabel>
#include <QTimer>
#include <QWidget>
#include <array>

extern MyConfig global_config;

void gaze_data_callback(TobiiResearchGazeData *tr_gaze_data, void *user_data);

class ImageShowWidget : public QWidget
{
    Q_OBJECT
public:
    explicit ImageShowWidget(QWidget *parent = nullptr);
    void init_ui();
    void init_timer();
    void init_connections();
    void load_config();
    void load_images();
    void subscribe_eye_data();
    void save_eye_data(const QString &);

signals:
    void eye_detection_error(QString);
    void experiment_error(QString);
    void experiment_pause(QString);
    void experiment_finished(QString);
    void show_score_page();
    void set_score_page_edit_content(QString,QString);

public slots:
    void begin_test(QString);
    void continue_test(QString);
    void pause(QString);
    void score_submit(int);

private slots:
    void do_timer_timeout();
    void do_error_detection();
    void save_score();

private:
    virtual void keyReleaseEvent(QKeyEvent *) override;
    enum DisplayState
    {
        START = 0,
        READY = 1,
        IMAGE = 2,
        ERROR = 3,
        FINISH = 4
    };
    uint state;
    int countdown;
    MyPoint2D resolution;
    ScorePage* score_page;
    QLayout *image_layout;
    QLabel *image_display;
    QTimer *imgshow_timer;
    QTimer *detect_error_timer;
    EyeTrackerWrapper *eyetracker_wrap;
    // some const use config variables
    int eyetracker_frequency;
    int image_show_time;
    int image_show_interval;
    int detect_error_interval_ms;
    int imgshow_timer_interval_ms;
    int eye_detect_error_count;
    bool is_debug;
    QString dir_imgdb;
    QString dir_out_data;
    QList<QString> image_suffix;
    // some image identify variables
    int image_num;
    QList<QString> image_list;
    int cur_image_index;
    QImage cur_image;
    QPixmap cur_pixmap;
    QString current_eye_data_file_name;
    QString cur_image_name;
    QString cur_image_file;
    bool is_subscribed;
    QString participant_id;
    int cur_image_score;
};

#endif // IMAGESHOWWIDGET_H
