
////////////////////////////////////////////////////////////////////////
//
//                 Cambridge Crystallographic Data Centre
//                                CCDC 
//
////////////////////////////////////////////////////////////////////////
//
// For information on free software for rendering this file to create very
// high quality bitmap images, please visit the POV-Ray website:
// www.povray.org.
//
// This POV-Ray output mechanism has been tested with POV-Ray version 3.7.
//
// The CCDC is keen to receive feedback on, and suggestions for improvements
// to, this POV-Ray output mechanism. Please visit www.ccdc.cam.ac.uk,
// or e-mail feedback to support@ccdc.cam.ac.uk. Thank you.
//
////////////////////////////////////////////////////////////////////////
//
// If this POVRay file has been generated from an entry in the Cambridge 
// Structural Database, then it will include bibliographic, chemical, crystal, 
// experimental, refinement or atomic coordinate data resulting from the CCDC's 
// data processing and validation procedures.
//
////////////////////////////////////////////////////////////////////////

#version 3.7;
global_settings {
    assumed_gamma 2.2
    max_trace_level 5
}

// -----------------------------------------------------------

#macro rotate_view_for_animation()
    // If using the [filename.pov].ini file, with animation enabled, this will produce
    // a cyclic animation of the scene rotating, otherwise this will not affect the image:
    rotate <0,clock*360,0>
#end

#macro ccdc_perspective_camera( camera_position, field_of_view )
    camera {
        perspective
        location camera_position
        up    <0,1,0>
        right  -x * (image_width/image_height)
        look_at <0,0,-100>
        // Convert the vertical field of view to the horizontal field of view
        angle degrees(2 * atan2(tan(radians(field_of_view / 2)) * image_width, image_height))

        rotate_view_for_animation()
    }
#end

#macro ccdc_directional_light_source( light_position, light_diffuse_colour, light_specular_colour )
    // The scalar multiplier applied to light_position seems to be needed for correct brightness
    light_source {
        5 * light_position
        light_diffuse_colour
        parallel
        shadowless
        rotate_view_for_animation()
    }
    light_source {
        5 * light_position
        light_specular_colour
        parallel
        rotate_view_for_animation()
    }
#end

#macro ccdc_ambient_light_source( light_colour )
    global_settings { ambient_light light_colour * 10 }
#end

#macro ccdc_background_colour( background_colour )
    background { background_colour }
#end

#macro ccdc_background_gradient( top_right_colour, top_left_colour, bottom_left_colour, bottom_right_colour )
    // TODO - adjust to use all four colours
    background { bottom_left_colour }
#end

#macro ccdc_orient_world( world_orientation )
    transform { world_orientation }
#end

#macro ccdc_orient_structure( structure_orientation )
    transform { structure_orientation }
#end

#macro ccdc_set_standard_mercury_solid_material_properties( object_color )
    no_shadow
    texture {
        pigment { object_color }
        finish {
            specular 0.2
            roughness 0.02
        }
    }
#end

#macro ccdc_set_shiny_solid_material_properties( object_color )
    no_shadow
    texture {
        pigment { object_color }
        finish {
            specular 0.8
            roughness 0.02
        }
    }
#end

#macro ccdc_set_matt_solid_material_properties( object_color )
    no_shadow
    texture {
        pigment { object_color }
        finish {
            specular 0.0
            roughness 0.02
        }
    }
#end

#macro ccdc_set_metallic_solid_material_properties( object_color )
    no_shadow
    texture {
        pigment { object_color }
        finish {
            ambient 0.2
            diffuse 0.2
            specular 1.0
            roughness 0.02 
            metallic
            reflection { 0.5, 1.0
               fresnel on
               metallic 0.8
            }
        }
    }
#end

#macro ccdc_set_iridescent_solid_material_properties( object_color )
    no_shadow
    texture {
        pigment { object_color }
        finish {
            ambient 0.1
            diffuse 0.1
            reflection 0.2
            specular 1
            roughness 0.02
            irid {
              0.35
              thickness 0.5
              turbulence 0.5
            }
        }
    }
#end

#macro ccdc_set_solid_material_properties( object_color )
    // change the method call here to select different properties settings
    ccdc_set_standard_mercury_solid_material_properties( object_color )
#end

#macro ccdc_set_wireframe_material_properties( object_color )
    no_shadow
    pigment { object_color }
#end

#macro ccdc_set_point_size( point_size )
    // TODO
#end

#macro ccdc_draw_circle( centre, circle_radius, transformation, circle_color )
    torus {
        circle_radius, 0.03
        transform { transformation }
        translate centre
        ccdc_set_wireframe_material_properties( circle_color )
    }
#end

#macro ccdc_draw_wireframe_sphere( centre, sphere_radius, sphere_color )
    union {
        #local transformation = transform { matrix <
            0, -1, 0,
            1, 0, 0,
            0, 0, 1,
            0, 0, 0 > };
        ccdc_draw_circle( centre, sphere_radius, transformation, sphere_color )
        #local transformation = transform { matrix <
            1, 0, 0,
            0, 1, 0,
            0, 0, 1,
            0, 0, 0 > };
        ccdc_draw_circle( centre, sphere_radius, transformation, sphere_color )
        #local transformation = transform { matrix <
            1, 0, 0,
            0, 0, 1,
            0, -1, 0,
            0, 0, 0 > };
        ccdc_draw_circle( centre, sphere_radius, transformation, sphere_color )
        #local transformation = transform { matrix <
            1, 0, 0,
            0, 0.707107, 0.707107,
            0, -0.707107, 0.707107,
            0, 0, 0 > };
        ccdc_draw_circle( centre, sphere_radius, transformation, sphere_color )
        #local transformation = transform { matrix <
            0.5, -0.707107, -0.5,
            0.707107, 0, 0.707107,
            -0.5, -0.707107, 0.5,
            0, 0, 0 > };
        ccdc_draw_circle( centre, sphere_radius, transformation, sphere_color )
        #local transformation = transform { matrix <
            0.707107, -0.707107, 0,
            0.707107, 0.707107, 0,
            0, 0, 1,
            0, 0, 0 > };
        ccdc_draw_circle( centre, sphere_radius, transformation, sphere_color )
        #local transformation = transform { matrix <
            1, 0, 0,
            0, -0.707107, 0.707107,
            0, -0.707107, -0.707107,
            0, 0, 0 > };
        ccdc_draw_circle( centre, sphere_radius, transformation, sphere_color )
        #local transformation = transform { matrix <
            0.5, 0.707107, 0.5,
            -0.707107, 0, 0.707107,
            0.5, -0.707107, 0.5,
            0, 0, 0 > };
        ccdc_draw_circle( centre, sphere_radius, transformation, sphere_color )
        #local transformation = transform { matrix <
            0.707107, 0.707107, 0,
            -0.707107, 0.707107, 0,
            0, 0, 1,
            0, 0, 0 > };
        ccdc_draw_circle( centre, sphere_radius, transformation, sphere_color )

    }
#end

#macro ccdc_draw_solid_sphere( position, sphere_radius, sphere_color )
    sphere {
        position, sphere_radius
        ccdc_set_solid_material_properties( sphere_color )
    }
#end

#macro ccdc_draw_solid_polygon( vertices, origin, transformation, polygon_color )
    #local nvertices = dimension_size( vertices, 1 );
    polygon {
        nvertices + 1
        #local i = 0;
        #while ( i < nvertices )
            vertices[ i ]
            #local i = i + 1;
        #end
        // Repeat the first point, to close the polygon:
        vertices[ 0 ]
        translate origin
        transform { transformation inverse }
        ccdc_set_solid_material_properties( polygon_color )
    }
#end

#macro ccdc_draw_solid_torus( centre, ring_radius, torus_radius, transformation, torus_color )
    torus {
        ring_radius, torus_radius
        transform { transformation }
        translate centre
        ccdc_set_solid_material_properties( torus_color )
    }
#end

#macro ccdc_draw_disk( centre, disk_radius, disk_normal, disk_color )
    // TODO
#end

#macro ccdc_draw_line_segment( line_begin, line_end, line_color )
    cylinder {
        line_begin, line_end, 0.03
        ccdc_set_wireframe_material_properties( line_color )
    }
#end

#macro ccdc_draw_stippled_line_segment( line_begin, line_end, stipple, stipple_scale_factor, line_color )
    // TODO - adjust to use stipple and stipple_scale_factor
    /* For example:

        AACRUB delocalised bonds:
        61680 = F0F0
        
        AABHTZ contacts:
        43690 = AAAA
    */
    // The following is approximately correct when drawing contacts
    #declare nsteps = 20;
    #declare increment = 1 / nsteps;
    #declare scalar1 = 0.0;
    #while ( scalar1 < 1.0 )
        #declare point1 = ( scalar1 * line_begin ) + ( 1 - scalar1 ) * line_end;
        #declare scalar2 = scalar1 + ( increment / 2.0 );
        #declare point2 = ( scalar2 * line_begin ) + ( 1 - scalar2 ) * line_end;
        cylinder {
            point1, point2, 0.03
            ccdc_set_wireframe_material_properties( line_color )
        }
        #declare scalar1 = scalar1 + increment;
    #end
#end

#macro ccdc_draw_wireframe_arc( arc_centre, arc_end_1, arc_end_2,
                                stipple, stipple_scale_factor, line_color )
    // TODO
#end

#macro ccdc_draw_wireframe_ellipsoid( centre, axis1, axis2, axis3, ellipsoid_colour )
    union {
        #local circle_radius = 1.0;
        #local origin = < 0, 0, 0 >;

        #local transformation = transform { matrix <
            0, -1, 0,
            1, 0, 0,
            0, 0, 1,
            0, 0, 0 > };
        ccdc_draw_circle( origin, circle_radius, transformation, ellipsoid_colour )
        #local transformation = transform { matrix <
            1, 0, 0,
            0, 1, 0,
            0, 0, 1,
            0, 0, 0 > };
        ccdc_draw_circle( origin, circle_radius, transformation, ellipsoid_colour )
        #local transformation = transform { matrix <
            1, 0, 0,
            0, 0, 1,
            0, -1, 0,
            0, 0, 0 > };
        ccdc_draw_circle( origin, circle_radius, transformation, ellipsoid_colour )
        #local transformation = transform { matrix <
            1, 0, 0,
            0, 0.707107, 0.707107,
            0, -0.707107, 0.707107,
            0, 0, 0 > };
        ccdc_draw_circle( origin, circle_radius, transformation, ellipsoid_colour )
        #local transformation = transform { matrix <
            0.5, -0.707107, -0.5,
            0.707107, 0, 0.707107,
            -0.5, -0.707107, 0.5,
            0, 0, 0 > };
        ccdc_draw_circle( origin, circle_radius, transformation, ellipsoid_colour )
        #local transformation = transform { matrix <
            0.707107, -0.707107, 0,
            0.707107, 0.707107, 0,
            0, 0, 1,
            0, 0, 0 > };
        ccdc_draw_circle( origin, circle_radius, transformation, ellipsoid_colour )
        #local transformation = transform { matrix <
            1, 0, 0,
            0, -0.707107, 0.707107,
            0, -0.707107, -0.707107,
            0, 0, 0 > };
        ccdc_draw_circle( origin, circle_radius, transformation, ellipsoid_colour )
        #local transformation = transform { matrix <
            0.5, 0.707107, 0.5,
            -0.707107, 0, 0.707107,
            0.5, -0.707107, 0.5,
            0, 0, 0 > };
        ccdc_draw_circle( origin, circle_radius, transformation, ellipsoid_colour )
        #local transformation = transform { matrix <
            0.707107, 0.707107, 0,
            -0.707107, 0.707107, 0,
            0, 0, 1,
            0, 0, 0 > };
        ccdc_draw_circle( origin, circle_radius, transformation, ellipsoid_colour )

        scale < vlength( axis1 ), vlength( axis2 ), vlength( axis3 ) >
        #declare axis1_norm = vnormalize( axis1 );
        #declare axis2_norm = vnormalize( axis2 );
        #declare axis3_norm = vnormalize( axis3 );
        matrix < axis1_norm.x,  axis1_norm.y,  axis1_norm.z,
                 axis2_norm.x,  axis2_norm.y,  axis2_norm.z,
                 axis3_norm.x,  axis3_norm.y,  axis3_norm.z,
                 0, 0, 0 >

        translate centre
    }
#end

#macro ccdc_draw_open_cylinder( centre_line_begin, centre_line_end, cylinder_radius, cylinder_color )
    cylinder {
        centre_line_begin, centre_line_end, cylinder_radius
        open
        ccdc_set_solid_material_properties( cylinder_color )
    }
#end

#macro ccdc_draw_closed_cylinder( centre_line_begin, centre_line_end, cylinder_radius, cylinder_color )
    cylinder {
        centre_line_begin, centre_line_end, cylinder_radius
        ccdc_set_solid_material_properties( cylinder_color )
    }
#end

#macro ccdc_draw_solid_ellipsoid( centre, axis1, axis2, axis3, ellipsoid_color )
    sphere {
        < 0, 0, 0 >, 1
        scale < vlength( axis1 ), vlength( axis2 ), vlength( axis3 ) >
        #declare axis1_norm = vnormalize( axis1 );
        #declare axis2_norm = vnormalize( axis2 );
        #declare axis3_norm = vnormalize( axis3 );
        matrix < axis1_norm.x,  axis1_norm.y,  axis1_norm.z,
                 axis2_norm.x,  axis2_norm.y,  axis2_norm.z,
                 axis3_norm.x,  axis3_norm.y,  axis3_norm.z,
                 0, 0, 0 >
        translate centre
        ccdc_set_solid_material_properties( ellipsoid_color )
    }
#end

#macro ccdc_draw_ellipsoid_axes( centre, axis1, axis2, axis3, axes_color )
    union {
        cylinder {
            < 0.05, 0, 0 >, < -0.05, 0, 0 >, 1
        }
        cylinder {
            < 0, 0.05, 0 >, < 0, -0.05, 0 >, 1
        }
        cylinder {
            < 0, 0, 0.05 >, < 0, 0, -0.05 >, 1
        }
        #local axis_height = 0.01;
        scale < vlength( axis1 ) + axis_height, vlength( axis2 ) + axis_height, vlength( axis3 ) + axis_height >
        #declare axis1_norm = vnormalize( axis1 );
        #declare axis2_norm = vnormalize( axis2 );
        #declare axis3_norm = vnormalize( axis3 );
        matrix < axis1_norm.x,  axis1_norm.y,  axis1_norm.z,
                 axis2_norm.x,  axis2_norm.y,  axis2_norm.z,
                 axis3_norm.x,  axis3_norm.y,  axis3_norm.z,
                 0, 0, 0 >
        translate centre
        ccdc_set_solid_material_properties( axes_color )
    }
#end

#macro ccdc_draw_point( point_location, point_color )
    // TODO
#end

#macro ccdc_draw_solid_triangle( corner1, corner2, corner3,
                                 color1, color2, color3,
                                 normal1, normal2, normal3 )
   smooth_triangle {
        corner1, normal1,
        corner2, normal2,
        corner3, normal3
        ccdc_set_solid_material_properties( color1 )
        // TODO POVRay does not appear to support different colours for 
        //      different vertices in a smooth_triangle
        //      See section 3.5.8 of the POVRay help.
   }
#end

#macro ccdc_draw_solid_triangle_without_normals( corner1, corner2, corner3,
                                                 color1, color2, color3 )
   triangle {
        corner1,
        corner2,
        corner3
        ccdc_set_solid_material_properties( color1 )
        // TODO POVRay does not appear to support different colours for 
        //      different vertices in a smooth_triangle
        //      See section 3.5.8 of the POVRay help.
   }
#end

#macro ccdc_draw_text( position, message, text_color, text_offset )
    // TODO - Adjust so that the text orientation is correct
    text { ttf font_name, message, 0.1, 0
        ccdc_set_wireframe_material_properties( color text_color )
        /*
        finish {
            ambient 0.2
            diffuse 0.6
            phong 0.3
            phong_size 100
        }
        */
        scale < font_scale, font_scale, font_scale >
        // rotate so text always faces the camera when animated
        rotate <0,clock*360,0>
        translate text_offset
        transform { world_rotation inverse }
        transform { structure_rotation inverse }
        translate position
    }
#end

#macro ccdc_draw_static_text( message )
    // TODO
#end

// -----------------------------------------------------------

// You can edit the file "ccdc_macro_overrides.inc" in this directory
// to override the implementations of any or all the above POVRay macros:
#include "ccdc_macro_overrides.inc"

#declare font_scale = 0.370397;

#declare font_name = "cyrvetic.ttf";

ccdc_perspective_camera( < 0, 0, 21222.2 >, 0.05 )
ccdc_directional_light_source( < 1, 1, 1 >, rgb < 0.7, 0.7, 0.7 >, rgb < 1, 1, 1 > )
ccdc_directional_light_source( < -1, 0.2, 1 >, rgb < 0.5, 0.5, 0.5 >, rgb < 0.5, 0.5, 0.5 > )
ccdc_ambient_light_source( rgb < 0.3, 0.3, 0.3 > )
ccdc_background_colour( rgb < 1, 1, 1 > )
union {
    #declare world_orientation = transform { matrix <
        -0.118224, -0.00770838, 0.992957,
        -0.970755, -0.209518, -0.117207,
        0.208946, -0.977774, 0.0172872,
        -6.2479, 64.085, -27.8287 > };
    #declare world_rotation = transform { matrix <
        -0.118224, -0.00770838, 0.992957,
        -0.970755, -0.209518, -0.117207,
        0.208946, -0.977774, 0.0172872,
        0, 0, 0 > };
    union {
        // A:LZ11301
        #declare structure_orientation = transform { matrix <
            1, 0, 0,
            0, 1, 0,
            0, 0, 1,
            0, 0, 0 > };
        #declare structure_rotation = transform { matrix <
            1, 0, 0,
            0, 1, 0,
            0, 0, 1,
            0, 0, 0 > };
        // A:LZ11301 atoms
        // atom C1
        ccdc_draw_solid_sphere( < 26.6475, 4.43, 64.2625 >, 0.1, rgb < 0.57, 0.57, 0.57 > )
        // atom C2
        ccdc_draw_solid_sphere( < 27.3295, 5.65, 64.3745 >, 0.1, rgb < 0.57, 0.57, 0.57 > )
        // atom C3
        ccdc_draw_solid_sphere( < 26.8645, 6.738, 63.6395 >, 0.1, rgb < 0.57, 0.57, 0.57 > )
        // atom C4
        ccdc_draw_solid_sphere( < 25.7625, 6.612, 62.8126 >, 0.1, rgb < 0.57, 0.57, 0.57 > )
        // atom C5
        ccdc_draw_solid_sphere( < 25.1035, 5.401, 62.7056 >, 0.1, rgb < 0.57, 0.57, 0.57 > )
        // atom C6
        ccdc_draw_solid_sphere( < 25.5455, 4.309, 63.4255 >, 0.1, rgb < 0.57, 0.57, 0.57 > )
        // atom N
        ccdc_draw_solid_sphere( < 27.3085, 3.547, 65.0775 >, 0.1, rgb < 0.56, 0.56, 1 > )
        // atom C9
        ccdc_draw_solid_sphere( < 28.3846, 5.413, 65.2895 >, 0.1, rgb < 0.57, 0.57, 0.57 > )
        // atom N2
        ccdc_draw_solid_sphere( < 28.3646, 4.137, 65.6975 >, 0.1, rgb < 0.56, 0.56, 1 > )
        // atom H1
        ccdc_draw_solid_sphere( < 27.3736, 7.6976, 63.7166 >, 0.1, rgb < 1, 1, 1 > )
        // atom H2
        ccdc_draw_solid_sphere( < 25.4121, 7.4713, 62.2427 >, 0.1, rgb < 1, 1, 1 > )
        // atom H3
        ccdc_draw_solid_sphere( < 24.2361, 5.3086, 62.0536 >, 0.1, rgb < 1, 1, 1 > )
        // atom H4
        ccdc_draw_solid_sphere( < 25.0306, 3.3535, 63.3373 >, 0.1, rgb < 1, 1, 1 > )
        // atom H5
        ccdc_draw_solid_sphere( < 29.1074, 6.1599, 65.6144 >, 0.1, rgb < 1, 1, 1 > )
        // atom H6
        ccdc_draw_solid_sphere( < 27.0427, 2.5754, 65.2021 >, 0.1, rgb < 1, 1, 1 > )
        // A:LZ11301 bonds
        // bond C1-C2
        ccdc_draw_closed_cylinder( < 26.6475, 4.43, 64.2625 >, < 27.3295, 5.65, 64.3745 >, 0.1, rgb < 0.57, 0.57, 0.57 > )
        // bond C1-C6
        ccdc_draw_closed_cylinder( < 26.6475, 4.43, 64.2625 >, < 25.5455, 4.309, 63.4255 >, 0.1, rgb < 0.57, 0.57, 0.57 > )
        // bond C1-N
        ccdc_draw_closed_cylinder( < 26.6475, 4.43, 64.2625 >, < 26.978, 3.9885, 64.67 >, 0.1, rgb < 0.57, 0.57, 0.57 > )
        ccdc_draw_closed_cylinder( < 26.978, 3.9885, 64.67 >, < 27.3085, 3.547, 65.0775 >, 0.1, rgb < 0.56, 0.56, 1 > )
        // bond C2-C3
        ccdc_draw_closed_cylinder( < 27.3295, 5.65, 64.3745 >, < 26.8645, 6.738, 63.6395 >, 0.1, rgb < 0.57, 0.57, 0.57 > )
        // bond C2-C9
        ccdc_draw_closed_cylinder( < 27.3295, 5.65, 64.3745 >, < 28.3846, 5.413, 65.2895 >, 0.1, rgb < 0.57, 0.57, 0.57 > )
        // bond C3-C4
        ccdc_draw_closed_cylinder( < 26.8645, 6.738, 63.6395 >, < 25.7625, 6.612, 62.8126 >, 0.1, rgb < 0.57, 0.57, 0.57 > )
        // bond C4-C5
        ccdc_draw_closed_cylinder( < 25.7625, 6.612, 62.8126 >, < 25.1035, 5.401, 62.7056 >, 0.1, rgb < 0.57, 0.57, 0.57 > )
        // bond C5-C6
        ccdc_draw_closed_cylinder( < 25.1035, 5.401, 62.7056 >, < 25.5455, 4.309, 63.4255 >, 0.1, rgb < 0.57, 0.57, 0.57 > )
        // bond N-N2
        ccdc_draw_closed_cylinder( < 27.3085, 3.547, 65.0775 >, < 28.3646, 4.137, 65.6975 >, 0.1, rgb < 0.56, 0.56, 1 > )
        // bond C9-N2
        ccdc_draw_closed_cylinder( < 28.4597, 5.42904, 65.3433 >, < 28.4497, 4.79104, 65.5473 >, 0.075, rgb < 0.57, 0.57, 0.57 > )
        ccdc_draw_closed_cylinder( < 28.3095, 5.39696, 65.2357 >, < 28.2995, 4.75896, 65.4397 >, 0.075, rgb < 0.57, 0.57, 0.57 > )
        ccdc_draw_closed_cylinder( < 28.4497, 4.79104, 65.5473 >, < 28.4397, 4.15304, 65.7513 >, 0.075, rgb < 0.56, 0.56, 1 > )
        ccdc_draw_closed_cylinder( < 28.2995, 4.75896, 65.4397 >, < 28.2895, 4.12096, 65.6437 >, 0.075, rgb < 0.56, 0.56, 1 > )
        // bond C3-H1
        ccdc_draw_closed_cylinder( < 26.8645, 6.738, 63.6395 >, < 27.1191, 7.2178, 63.678 >, 0.1, rgb < 0.57, 0.57, 0.57 > )
        ccdc_draw_closed_cylinder( < 27.1191, 7.2178, 63.678 >, < 27.3736, 7.6976, 63.7166 >, 0.1, rgb < 1, 1, 1 > )
        // bond C4-H2
        ccdc_draw_closed_cylinder( < 25.7625, 6.612, 62.8126 >, < 25.5873, 7.04165, 62.5277 >, 0.1, rgb < 0.57, 0.57, 0.57 > )
        ccdc_draw_closed_cylinder( < 25.5873, 7.04165, 62.5277 >, < 25.4121, 7.4713, 62.2427 >, 0.1, rgb < 1, 1, 1 > )
        // bond C5-H3
        ccdc_draw_closed_cylinder( < 25.1035, 5.401, 62.7056 >, < 24.6698, 5.3548, 62.3796 >, 0.1, rgb < 0.57, 0.57, 0.57 > )
        ccdc_draw_closed_cylinder( < 24.6698, 5.3548, 62.3796 >, < 24.2361, 5.3086, 62.0536 >, 0.1, rgb < 1, 1, 1 > )
        // bond C6-H4
        ccdc_draw_closed_cylinder( < 25.5455, 4.309, 63.4255 >, < 25.288, 3.83125, 63.3814 >, 0.1, rgb < 0.57, 0.57, 0.57 > )
        ccdc_draw_closed_cylinder( < 25.288, 3.83125, 63.3814 >, < 25.0306, 3.3535, 63.3373 >, 0.1, rgb < 1, 1, 1 > )
        // bond C9-H5
        ccdc_draw_closed_cylinder( < 28.3846, 5.413, 65.2895 >, < 28.746, 5.78645, 65.452 >, 0.1, rgb < 0.57, 0.57, 0.57 > )
        ccdc_draw_closed_cylinder( < 28.746, 5.78645, 65.452 >, < 29.1074, 6.1599, 65.6144 >, 0.1, rgb < 1, 1, 1 > )
        // bond N-H6
        ccdc_draw_closed_cylinder( < 27.3085, 3.547, 65.0775 >, < 27.1756, 3.0612, 65.1398 >, 0.1, rgb < 0.56, 0.56, 1 > )
        ccdc_draw_closed_cylinder( < 27.1756, 3.0612, 65.1398 >, < 27.0427, 2.5754, 65.2021 >, 0.1, rgb < 1, 1, 1 > )
        #local transformation = transform { matrix <
            0.715543, 0.598555, 0.36018,
            -0.598555, 0.259482, 0.757893,
            0.36018, -0.757893, 0.543939,
            0, 0, 0 > };
        ccdc_draw_solid_torus( < 26.2088, 5.52333, 63.5367 >, 0.690784, 0.05, transformation, rgb < 0.57, 0.57, 0.57 > )
        ccdc_draw_wireframe_sphere( < 27.3085, 3.547, 65.0775 >, 0.13, rgb < 1, 1, 0 > )
        ccdc_draw_solid_sphere( < 28.3646, 4.137, 65.6975 >, 0.25, rgbt < 1, 0, 0, 0.4 > )
        ccdc_draw_stippled_line_segment( < 28.3646, 4.137, 65.6975 >, < 30.1501, 2.92237, 67.4798 >, 43690, 1, rgb < 1, 1, 1 > )
        ccdc_draw_solid_sphere( < 28.3646, 4.137, 65.6975 >, 0.25, rgbt < 1, 0, 0, 0.4 > )
        ccdc_draw_solid_sphere( < 30.1501, 2.92237, 67.4798 >, 0.25, rgbt < 1, 0, 0, 0.7 > )
        ccdc_draw_stippled_line_segment( < 28.3846, 5.413, 65.2895 >, < 30.2431, 7.33345, 66.1249 >, 43690, 1, rgb < 1, 1, 1 > )
        ccdc_draw_solid_sphere( < 28.3846, 5.413, 65.2895 >, 0.25, rgbt < 0, 0, 1, 0.4 > )
        ccdc_draw_solid_sphere( < 30.2431, 7.33345, 66.1249 >, 0.25, rgbt < 0, 0, 1, 0.7 > )
        ccdc_draw_stippled_line_segment( < 27.3085, 3.547, 65.0775 >, < 26.5752, 0.866667, 65.4212 >, 43690, 1, rgb < 1, 1, 1 > )
        ccdc_draw_solid_sphere( < 27.3085, 3.547, 65.0775 >, 0.25, rgbt < 0, 0, 1, 0.4 > )
        ccdc_draw_solid_sphere( < 26.5752, 0.866667, 65.4212 >, 0.25, rgbt < 0, 0, 1, 0.7 > )
        ccdc_orient_structure( structure_orientation )
        #declare structure_orientation = transform { matrix <
            1, 0, 0,
            0, 1, 0,
            0, 0, 1,
            0, 0, 0 > };
        #declare structure_rotation = transform { matrix <
            1, 0, 0,
            0, 1, 0,
            0, 0, 1,
            0, 0, 0 > };
    }
    // A:LZ11301 finished
    union {
        // lz1
        #declare structure_orientation = transform { matrix <
            1, 0, 0,
            0, 1, 0,
            0, 0, 1,
            0, 0, 0 > };
        #declare structure_rotation = transform { matrix <
            1, 0, 0,
            0, 1, 0,
            0, 0, 1,
            0, 0, 0 > };
        // lz1 atoms
        // lz1 bonds
        ccdc_draw_wireframe_sphere( < 26.2088, 5.52333, 63.5367 >, 1, rgb < 0.333333, 1, 0 > )
        ccdc_draw_wireframe_sphere( < 26.2088, 5.52333, 63.5367 >, 1, rgb < 0.333333, 1, 0 > )
        ccdc_draw_line_segment( < 26.2088, 5.52333, 63.5367 >, < 27.8848, 4.79678, 61.4146 >, rgbt < 0.333333, 1, 0, 0.5 > )
        ccdc_draw_solid_sphere( < 27.8848, 4.79678, 61.4146 >, 1, rgbt < 0.333333, 1, 0, 0.5 > )
        ccdc_draw_wireframe_sphere( < 26.2088, 5.52333, 63.5367 >, 1, rgb < 0.333333, 1, 0 > )
        ccdc_draw_line_segment( < 26.2088, 5.52333, 63.5367 >, < 24.5329, 6.24988, 65.6588 >, rgbt < 0.333333, 1, 0, 0.5 > )
        ccdc_draw_solid_sphere( < 24.5329, 6.24988, 65.6588 >, 1, rgbt < 0.333333, 1, 0, 0.5 > )
        ccdc_draw_wireframe_sphere( < 27.6069, 4.6354, 64.9403 >, 1, rgb < 0.333333, 1, 0 > )
        ccdc_draw_line_segment( < 27.6069, 4.6354, 64.9403 >, < 25.9414, 5.35882, 67.0716 >, rgbt < 0.333333, 1, 0, 0.5 > )
        ccdc_draw_solid_sphere( < 25.9414, 5.35882, 67.0716 >, 1, rgbt < 0.333333, 1, 0, 0.5 > )
        ccdc_draw_wireframe_sphere( < 27.6069, 4.6354, 64.9403 >, 1, rgb < 0.333333, 1, 0 > )
        ccdc_draw_line_segment( < 27.6069, 4.6354, 64.9403 >, < 29.2725, 3.91198, 62.809 >, rgbt < 0.333333, 1, 0, 0.5 > )
        ccdc_draw_solid_sphere( < 29.2725, 3.91198, 62.809 >, 1, rgbt < 0.333333, 1, 0, 0.5 > )
        ccdc_draw_wireframe_sphere( < 28.3846, 5.413, 65.2895 >, 1, rgb < 0, 0, 1 > )
        ccdc_draw_line_segment( < 28.3846, 5.413, 65.2895 >, < 30.2431, 7.33345, 66.1249 >, rgbt < 0, 0, 1, 0.5 > )
        ccdc_draw_solid_sphere( < 30.2431, 7.33345, 66.1249 >, 1, rgbt < 0, 0, 1, 0.5 > )
        ccdc_draw_wireframe_sphere( < 27.3085, 3.547, 65.0775 >, 1, rgb < 0, 0, 1 > )
        ccdc_draw_line_segment( < 27.3085, 3.547, 65.0775 >, < 26.5752, 0.866667, 65.4212 >, rgbt < 0, 0, 1, 0.5 > )
        ccdc_draw_solid_sphere( < 26.5752, 0.866667, 65.4212 >, 1, rgbt < 0, 0, 1, 0.5 > )
        ccdc_draw_wireframe_sphere( < 28.3646, 4.137, 65.6975 >, 1, rgb < 1, 0, 0 > )
        ccdc_draw_line_segment( < 28.3646, 4.137, 65.6975 >, < 30.1501, 2.92237, 67.4798 >, rgbt < 1, 0, 0, 0.5 > )
        ccdc_draw_solid_sphere( < 30.1501, 2.92237, 67.4798 >, 1, rgbt < 1, 0, 0, 0.5 > )
        ccdc_orient_structure( structure_orientation )
        #declare structure_orientation = transform { matrix <
            1, 0, 0,
            0, 1, 0,
            0, 0, 1,
            0, 0, 0 > };
        #declare structure_rotation = transform { matrix <
            1, 0, 0,
            0, 1, 0,
            0, 0, 1,
            0, 0, 0 > };
    }
    // lz1 finished
    ccdc_orient_world( world_orientation )
}
