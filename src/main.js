/*
Este é o arquivo que renderiza as imagens usando
Three.js.

*/
import "./styles.css";
import * as THREE from "three";



var OrbitControls = require('three-orbit-controls')(THREE)

import pano1 from './assets/teste1.jpeg'; // Essa é a ultima imagem retornada dos scripts python
import pano2 from './assets/teste2.jpeg'

import feet from './assets/feet.svg'
import { Vector3 } from "three";
import { TweenLite } from "gsap/gsap-core";

const container = document.body;

var camera, scene, renderer, controls;


class Scene{

  constructor()

}

init();
animate();

function init() {

  camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 1, 1000 );
  camera.position.set(1,0,0);

  scene = new THREE.Scene();
 
  const rayCaster = new THREE.Raycaster()
 
  
  var geometry = new THREE.SphereGeometry(50,32,42); 
  
  // Imagem original: https://live.staticflickr.com/65535/50091270432_dd1da38ee7_5k.jpg
  var texture = new THREE.TextureLoader().load(pano2);
  texture.wrapS = THREE.RepeatWrapping //Espelhando a imagem
  texture.repeat.x = -1

  var material = new THREE.MeshBasicMaterial( { map: texture, side: THREE.DoubleSide } );
  const sphere = new THREE.Mesh(geometry,material); //definindo o objeto sendo da forma de "geometry", e do material de "material"
  scene.add( sphere );

  


  //RENDER
  renderer = new THREE.WebGLRenderer();
  renderer.setPixelRatio( window.devicePixelRatio );
  renderer.setSize( window.innerWidth, window.innerHeight );
  document.body.appendChild( renderer.domElement );

  
  //CAMERA
  controls = new OrbitControls( camera, renderer.domElement );
  controls.minDistance = 0
  controls.maxDistance = 15.0
  

  //Redimencionamento da tela
  window.addEventListener( 'resize', onWindowResize, false );
  
  //Mudança do mouse ao mover a camera
  window.onmousedown = () => {document.body.style.cursor = "move";}
  window.onmouseup = () => {document.body.style.cursor = "pointer";}

  //adicionando Simbulo de "'andar' para"
  addTooltip(new Vector3(
    43.071192785453675, //Y
    -0.7644674190358015, //X
    24.916103487018965), //z
    'corredor' 
  );


  //função que adiciona simbulo em determinada posição
  function addTooltip(position, name){
    let spriteMap = new THREE.TextureLoader().load(feet);
    let spriteMaterial = new THREE.SpriteMaterial( {map: spriteMap} );
    let sprite = new THREE.Sprite( spriteMaterial ); 
    
    sprite.name = name;
    sprite.position.copy(position.clone().normalize().multiplyScalar(30))

    sprite.scale.multiplyScalar(3)

    scene.add( sprite );
  }

  //função de detecção de click
  function onclick(e){
   
    let mouse  = new THREE.Vector2(
      (e.clientX / window.innerWidth) * 2 - 1,
      - (e.clientY / window.innerHeight) * 2 + 1
    );
    
    rayCaster.setFromCamera(mouse,camera)
    let intersects = rayCaster.intersectObjects(scene.children)
    
    intersects.forEach((intersect) =>{
      if(intersect.object.type == 'Sprite'){
        material.transparent = true
        console.log(intersect.object.name)
        TweenLite.to(sphere.material,0.4,{
          opacity:0
        })
      }
    })
      /*
    let intersects = rayCaster.intersectObject(sphere)
    
    if(intersects.length > 0){
      console.log(intersects[0].point)
      addTooltip(intersects[0].point)
    }
    */
  
  }

 

  container.addEventListener('click',onclick)
}

function animate() {

  requestAnimationFrame( animate );
	renderer.render( scene, camera );
  controls.update();
}

function toggleFullScreen() {
    if ((document.fullScreenElement && document.fullScreenElement !== null) ||    
      (!document.mozFullScreen && !document.webkitIsFullScreen)){
          
      if (document.documentElement.requestFullScreen) {  
        document.documentElement.requestFullScreen();  
      } 
      
      else if (document.documentElement.mozRequestFullScreen) {  
        document.documentElement.mozRequestFullScreen();  
      } 
      else if (document.documentElement.webkitRequestFullScreen) {  
        document.documentElement.webkitRequestFullScreen(Element.ALLOW_KEYBOARD_INPUT);  
      }  
    } 
    else {  
      if (document.cancelFullScreen) {  
        document.cancelFullScreen();  
      } else if (document.mozCancelFullScreen) {  
        document.mozCancelFullScreen();  
      } else if (document.webkitCancelFullScreen) {  
        document.webkitCancelFullScreen();  
      }  
    }  
}

function onWindowResize() {
    
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();

  renderer.setSize( window.innerWidth, window.innerHeight );

}
