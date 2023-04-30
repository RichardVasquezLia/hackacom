import { Component } from '@angular/core';

import { Camera, CameraResultType, CameraSource } from '@capacitor/camera';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent {

  title = 'Front';
  image = '';
  constructor( private http: HttpClient){

  }

  async captureImage() {
    const image = await Camera.getPhoto({
      quality: 90,
      allowEditing: true,
      source: CameraSource.Camera,
      resultType: CameraResultType.Base64
    });

    if (image) {
      this.image = `data:image/jpeg;base64,${image.base64String}`!;
    }
  }
  async predecir() {  
    const url = `http://127.0.0.1:8000/plant`;
    this.http.post(url, this.image)
        .subscribe(res => {
          console.log(res);
        });
  }



}
