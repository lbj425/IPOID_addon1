#ifndef MYCONFIG_H
#define MYCONFIG_H

#include "eyetrackerwrapper.h"
#include <QFile>
#include <QHash>
#include <QJsonObject>
#include <QSettings>
#include <QVariant>
#include <QtDebug>
class MyConfig
{
public:
    MyConfig();
    MyConfig(const QString& config_file_str);
    MyConfig(const QJsonObject& config_in_qjson);
    MyConfig(const MyConfig &other) = delete;
    MyConfig& operator=(const MyConfig &other)= delete;

    void load_eyetracker(const QString &address = "");
    void set_value(const QString &key, const QVariant value);
    QVariant get_value(const QString &key, const QVariant default_value) const;
    EyeTrackerWrapper *get_eyetracker_wrapper() const;
    void dump(const QString &dump_file_name) const;
    QJsonObject toQJsonObject() const;

    ~MyConfig();

private:
    QVariantHash config_params;
    QString config_source;
    EyeTrackerWrapper *eyetracker_wrapper;

    void default_init();
};

#endif // MYCONFIG_H
