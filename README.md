# videoSplice
使用python将一段视频分割为多个
# 脚本的用法：

### jkeditor.py <input> <output_dir> <start_time> <end_time> <slice_duration>
### input : 待剪辑的视频。
### output_dir：输出剪辑片段的目录。
### start_time：开始的时间，即start_time之前的片段剪掉。'%H:%M:%S'的格式(小时:分钟:秒)。
### end_time: 结束的时间，即end_time之后的片段剪掉。
### slice_duration：每个片段的时长，单位秒(s)。
# 使用示例

jkeditor.py input.mp4 ./slices 00:00:05 00:06:00 15

