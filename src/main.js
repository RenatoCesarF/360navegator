import "./styles.css";
import * as THREE from "three";
var OrbitControls = require('three-orbit-controls')(THREE)

var camera, scene, renderer, controls;

init();
animate();

function init() {

    camera = new THREE.PerspectiveCamera( 70, window.innerWidth / window.innerHeight, 1, 1000 );
    camera.position.set(1,0,0);


    scene = new THREE.Scene();

    //Configurando a esfera e adicionando-a à cena
    var geometry = new THREE.SphereGeometry(50,32,32); //Formato do objeto'a
    var texture = new THREE.TextureLoader().load( 'https://live.staticflickr.com/4649/25595107287_ef3b2df7e4_k.jpg' );
    var material = new THREE.MeshBasicMaterial( { map: texture, side: THREE.DoubleSide } );
    const sphere = new THREE.Mesh(geometry,material); //definindo o objeto sendo da forma de "geometry", e do material de "material"
    scene.add( sphere );

    renderer = new THREE.WebGLRenderer();
    renderer.setPixelRatio( window.devicePixelRatio );
    renderer.setSize( window.innerWidth, window.innerHeight );
    document.body.appendChild( renderer.domElement );

    controls = new OrbitControls( camera, renderer.domElement );
    
    controls.minDistance = 0
    controls.maxDistance = 20.0
    

    window.addEventListener( 'resize', onWindowResize, false );
    
    //Mudança do mouse ao mover a camera
    window.onmousedown = () => {document.body.style.cursor = "move";}
    window.onmouseup = () => {document.body.style.cursor = "pointer";}
}

function onWindowResize() {

    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();

    renderer.setSize( window.innerWidth, window.innerHeight );

}

function animate() {

    requestAnimationFrame( animate );
	renderer.render( scene, camera );
	controls.update();
}