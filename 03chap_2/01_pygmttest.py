import pygmt
import os

work_path = "/home/ish/DataProcessing_TRC/data/"

def function1():
    pygmt.show_versions()
    out_file = os.path.join(work_path, "my_pygmt_map.pdf")
    region = [123, 132.6, 31, 39]
    fig = pygmt.Figure()
    fig.coast(region=region, shorelines=True)
    fig.show()
    fig.savefig(out_file)

def function2():
    out_file = os.path.join(work_path, "improved.pdf")
    region = [123, 132.6, 31, 39]           # 경도, 위도
    
    fig = pygmt.Figure()
    
    # 기본 지도 설정
    # M12c: 메르카토르 투영법 12cm 너비 , frame: 격자선과 레이블 설정
    fig.basemap(
        region=region,
        projection='M12c',
        frame=["afg", "+tMy GMT Map"])
    
    # 해안선 그리기
    # shorelines: 해안선 두께, resolution: 해상도
    fig.coast(land="oldlace", water="lightblue", 
              shorelines="0.5p", resolution="h")
    
    # map_scale 지도 축척 추가 
    fig.basemap(projection = "M12c",
                frame = "a1fg",
                map_scale = "g124.5/31.5+w200k+f+l")
    # 마커 추가 (삼각형)
    fig.plot(x=[125, 130], y=[35, 37], style="t0.3c", fill="blue", pen="0.5p")
    fig.text(x=125, y=36, text="Yellow Sea Buoy", font="10p,Helvetica-Bold", offset="0.5c/0.5c")
    
    fig.show()
    
    # 파일로 저장 (300 DPI 해상도)
    fig.savefig(out_file, dpi=300)


# function1()
function2()